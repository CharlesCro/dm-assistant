import reflex as rx
from ..my_google_auth import (
    GoogleAuthState,
    require_google_login,
)
from typing import Any
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

from ..my_google_auth import google_login, google_oauth_provider



class GoogleState(GoogleAuthState):
    @rx.var
    def user_picture(self) -> str:
        # 'picture' is the standard OIDC field for the Google profile image URL
        return self.tokeninfo.get("picture", "")
    
    @rx.var(cache=True)
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you"
        return "Not logged in."
