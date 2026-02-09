import reflex as rx
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import time
import os

# Google ADK imports
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types as genai_types

# Internal imports
from ..rag_agent.agent import root_agent
from ..my_google_auth import GoogleAuthState  # Accessing the Google Auth data

class ChatMessage(BaseModel):
    """Represents a single chat message."""
    role: str  # "user" or "assistant"
    content: str

# Global ADK components (not stored in state since they're not serializable)
_adk_runner: Optional[Runner] = None
_session_service: Optional[InMemorySessionService] = None

class ChatState(rx.State):
    """State management for the chatbot interface with Google ADK integration."""
    
    # Message history
    messages: List[ChatMessage] = []
    
    # UI state
    processing: bool = False
    current_input: str = ""
    
    # ADK Session Management
    adk_session_id: str = ""
    
    # User Identity (now a standard variable to avoid coroutine errors)
    user_id: str = ""
    
    # Configuration
    APP_NAME: str = "dm-assistant"
    
    def _ensure_adk_initialized(self):
        """Initialize ADK runner if not already done."""
        global _adk_runner, _session_service
        
        if _adk_runner is None:
            print(f"DEBUG: Initializing ADK runner for {self.APP_NAME}")
            agent = root_agent
            _session_service = InMemorySessionService()
            _adk_runner = Runner(
                agent=agent,
                app_name=self.APP_NAME,
                session_service=_session_service
            )
    
    async def _ensure_session_exists(self):
        """Ensure ADK session exists, create if needed, and link to Google ID."""
        global _adk_runner, _session_service
        
        self._ensure_adk_initialized()
        
        # 1. Correctly await the Google Auth state to get the user email
        auth_state = await self.get_state(GoogleAuthState)
        self.user_id = auth_state.tokeninfo.get("email", "anonymous")
        
        # Create new session ID if none exists
        if not self.adk_session_id:
            self.adk_session_id = f"reflex_adk_{int(time.time())}_{os.urandom(2).hex()}"
            print(f"DEBUG: Generated new session ID: {self.adk_session_id}")
        
        # Check if session exists in ADK using the dynamic user_id
        session = await _session_service.get_session(
            app_name=self.APP_NAME,
            user_id=self.user_id,
            session_id=self.adk_session_id
        )
        
        # Create session if it doesn't exist
        if not session:
            print(f"DEBUG: Creating new ADK session for {self.user_id}")
            initial_state = {
                "user_name": auth_state.tokeninfo.get("name"),
                "user_hobbies": None,
                "user_interests": None
            }
            await _session_service.create_session(
                app_name=self.APP_NAME,
                user_id=self.user_id,
                session_id=self.adk_session_id,
                state=initial_state
            )
    
    def new_chat(self):
        """Clear current conversation and reset ADK session."""
        self.messages = []
        self.current_input = ""
        self.adk_session_id = ""
    
    async def send_message(self):
        """Handle sending a message and clearing UI."""
        if not self.current_input.strip():
            return
        
        query = self.current_input
        self.current_input = ""
        
        # Ensure the text area clears immediately
        yield rx.set_value("chat_input_field", "")
        
        user_message = ChatMessage(role="user", content=query)
        self.messages.append(user_message)
        
        self.processing = True
        yield
        
        try:
            # This handles both auth and ADK session setup
            await self._ensure_session_exists()
            assistant_response = await self._run_adk_agent(query)
            self.messages.append(ChatMessage(role="assistant", content=assistant_response))
        except Exception as e:
            self.messages.append(ChatMessage(role="assistant", content=f"Error: {str(e)}"))
        finally:
            self.processing = False
            yield

    async def _run_adk_agent(self, user_message_text: str) -> str:
        """Run the Google ADK agent and return the response."""
        global _adk_runner
        
        print(f"DEBUG: Running ADK agent for user {self.user_id}")
        
        content = genai_types.Content(
            role='user',
            parts=[genai_types.Part(text=user_message_text)]
        )
        
        final_response_text = "[Agent encountered an issue]"
        
        async for event in _adk_runner.run_async(
            user_id=self.user_id, # Uses the unique Google Email
            session_id=self.adk_session_id,
            new_message=content
        ):
            if event.is_final_response():
                if event.content and event.content.parts and hasattr(event.content.parts[0], 'text'):
                    final_response_text = event.content.parts[0].text
                break
        
        return final_response_text