
from ..my_google_auth import google_login, google_oauth_provider
import reflex as rx
from .state import GoogleState
from ..my_google_auth import handle_google_login

def login_page():
    my_child = rx.vstack(
        # ... your existing index UI code ...
        rx.button(
            "Login with Google",
            on_click=handle_google_login(), # Use the hook caller
            size="3",
            variant="outline",
        ),
        # ...
    )

    # WRAP the entire return in the provider
    return google_oauth_provider(
        my_child
    )