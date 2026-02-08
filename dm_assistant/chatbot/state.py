import reflex as rx
from typing import List
import asyncio

class ChatMessage(rx.Base):
    """Represents a single chat message."""
    role: str  # "user" or "assistant"
    content: str

class ChatState(rx.State):
    """State management for the chatbot interface."""
    
    # Message history
    messages: List[ChatMessage] = []
    
    # UI state
    processing: bool = False
    current_input: str = ""
    
    def new_chat(self):
        """Clear current conversation."""
        self.messages = []
        self.current_input = ""
    
    async def send_message(self):
        """Handle sending a message and getting AI response."""
        if not self.current_input.strip():
            return
        
        # Add user message
        user_message = ChatMessage(
            role="user",
            content=self.current_input
        )
        self.messages.append(user_message)
        
        # Clear input and show processing
        query = self.current_input
        self.current_input = ""
        self.processing = True
        yield
        
        # Simulate processing delay
        await asyncio.sleep(0.5)
        
        # TODO: INTEGRATE LLM API CALL (OpenAI/Anthropic/Claude) HERE
        # Example integration point:
        # response = await call_llm_api(query)
        # For now, use a placeholder response
        
        assistant_response = self._get_placeholder_response(query)
        
        # Add assistant message
        assistant_message = ChatMessage(
            role="assistant",
            content=assistant_response
        )
        self.messages.append(assistant_message)
        
        self.processing = False
        yield
    
    def _get_placeholder_response(self, query: str) -> str:
        """Placeholder response until LLM is integrated."""
        return f"""I received your message: "{query}"

This is a placeholder response. To integrate a real LLM:

1. **OpenAI GPT**: Install `openai` and use:
   ```python
   import openai
   response = await openai.ChatCompletion.acreate(
       model="gpt-4",
       messages=[{{"role": "user", "content": query}}]
   )
   ```

2. **Anthropic Claude**: Install `anthropic` and use:
   ```python
   import anthropic
   client = anthropic.AsyncAnthropic(api_key="...")
   response = await client.messages.create(
       model="claude-3-5-sonnet-20241022",
       messages=[{{"role": "user", "content": query}}]
   )
   ```

Replace `_get_placeholder_response()` with your API call!"""
    
    def handle_key_down(self, key: str):
        """Handle Enter key to send message (Shift+Enter for new line)."""
        # Note: In Reflex, we check for "Enter" key
        # Shift+Enter is handled automatically by text_area
        if key == "Enter":
            return self.send_message()