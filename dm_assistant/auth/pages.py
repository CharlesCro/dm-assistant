
from ..my_google_auth import google_login, google_oauth_provider
import reflex as rx
from .state import GoogleState


def login_page():
    return rx.box(
        google_oauth_provider(
            google_login(),
        ),
    )