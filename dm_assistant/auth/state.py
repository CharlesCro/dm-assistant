from reflex_google_auth import GoogleAuthState, require_google_login
import reflex as rx

class MyAuthState(GoogleAuthState):
    @rx.var(cache=True)
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"This content can only be viewed by a logged in User. Nice to see you {self.tokeninfo['name']}"
        return "Not logged in."
    
    def do_logout(self):
        """Standard logout handler for reflex-google-auth."""
        # Clears the local storage token and resets state
        return rx.redirect("/") # Redirect to home/login after logout