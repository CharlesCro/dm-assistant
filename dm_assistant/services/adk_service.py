import reflex as rx
import asyncio
import time
import os
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types as genai_types

# Internal imports from your project
from ..rag_agent.agent import root_agent
from ..config.settings import APP_NAME_FOR_ADK, INITIAL_STATE
from ..my_google_auth import GoogleAuthState  # Accessing the Google Auth data

# Global runner initialization
# Note: The Runner is stateless; user isolation happens via the user_id passed at runtime.
_SESSION_SERVICE = InMemorySessionService()
_ADK_RUNNER = Runner(
    agent=root_agent,
    app_name=APP_NAME_FOR_ADK,
    session_service=_SESSION_SERVICE
)

class ADKState(rx.State):
    """The app state for managing isolated ADK interactions."""
    
    adk_session_id: str = ""
    chat_history: list[dict[str, str]] = []
    is_processing: bool = False

    async def on_load(self):
        """Initializes the ADK session using the Google Auth identity."""
        # 1. Access the Google Auth state to get the user's email
        auth_state = await self.get_state(GoogleAuthState)
        user_email = auth_state.tokeninfo.get("email")

        # 2. Safety check: If no user is logged in, do nothing (or redirect)
        if not user_email:
            return rx.redirect("/")

        if not self.adk_session_id:
            # Generate a unique session ID for this specific chat thread
            self.adk_session_id = f"reflex_adk_{int(time.time())}"
            
            # 3. Create the session using the Google Email as the USER_ID
            # This ensures the ADK engine isolates this user's RAG Corpora from others.
            await _SESSION_SERVICE.create_session(
                app_name=APP_NAME_FOR_ADK,
                user_id=user_email,
                session_id=self.adk_session_id,
                state=INITIAL_STATE
            )

    async def answer_question(self, user_message: str):
        """Sends a question to the agent within the user's isolated context."""
        if not user_message:
            return

        # Fetch the user's identity again for this specific event
        auth_state = await self.get_state(GoogleAuthState)
        user_email = auth_state.tokeninfo.get("email")
        
        if not user_email:
            return

        self.is_processing = True
        self.chat_history.append({"role": "user", "content": user_message})
        yield

        try:
            # Prepare ADK Content
            content = genai_types.Content(
                role='user', 
                parts=[genai_types.Part(text=user_message)]
            )

            response_text = "The agent encountered an issue."

            # 4. Run the Agent with the user_email as user_id.
            # Vertex AI RAG tools called by the agent will now be scoped to this ID.
            async for event in _ADK_RUNNER.run_async(
                user_id=user_email, 
                session_id=self.adk_session_id, 
                new_message=content
            ):
                if event.is_final_response():
                    if event.content and event.content.parts:
                        response_text = event.content.parts[0].text
                    break

            self.chat_history.append({"role": "assistant", "content": response_text})

        except Exception as e:
            self.chat_history.append({"role": "assistant", "content": f"Error: {str(e)}"})
        finally:
            self.is_processing = False