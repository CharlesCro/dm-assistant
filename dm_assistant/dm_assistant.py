import reflex as rx
from rxconfig import config
from .ui.base import base_page
from . import auth, session_summary, contact, navigation, pages, chatbot, character_sheet
import dm_assistant.styles as styles
from .auth.state import GoogleState


# 1. Removed the @require_google_login() decorator to make this page public
def index() -> rx.Component:
    
    # Welcome Page (Index)
    my_child = rx.vstack(
        rx.heading("Welcome to Dungeon Master Assistant!", weight="bold"),
        rx.text(
            "Dungeon Master Assistant is an AI-powered tool designed to help Dungeon Masters create and manage their Dungeons & Dragons campaigns with ease.",
            size="5",
        ),
        rx.hstack(
            rx.cond(
                GoogleState.token_is_valid,
                rx.text(f'Welcome {GoogleState.user_name}'),
                rx.link(
                rx.button(
                    "Login with Google", 
                    size="3", 
                    variant="outline",
                    color_scheme="blue",
                    cursor="pointer"
                ),
                href="/login",
            ),
            ),
            
            spacing="4",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='my-child'
    )

    return base_page(
        my_child
    )
from starlette.middleware.base import BaseHTTPMiddleware

# 1. Define a middleware class to set the COOP header
class COOPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        # This header allows Google's popup to communicate with your app
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin-allow-popups"
        return response

# 2. Define the transformer function
def apply_backend_middleware(api_app):
    api_app.add_middleware(COOPMiddleware)
    return api_app


app = rx.App(
    theme=styles.base_theme,
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEET,
    api_transformer=apply_backend_middleware
)

app.add_page(index, route='/', title="Home")
app.add_page(auth.login_page, route='/login', title='Login')
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE, title="About")
app.add_page(pages.files_page, route=navigation.routes.FILES_ROUTE, title="Files")
app.add_page(session_summary.session_summary_list_page, route=navigation.routes.SESSION_SUMMARIES_ROUTE, title="Session Summaries", on_load=session_summary.SessionSummaryState.load_summaries)
app.add_page(session_summary.session_summary_detail_page, route='/session-summaries/[session_id]', title="Session Summary Detail", on_load=session_summary.SessionSummaryState.get_summary_detail)
app.add_page(session_summary.session_summary_add_page, route=navigation.routes.ADD_SESSION_SUMMARY_ROUTE, title="Add Session Summary")
app.add_page(session_summary.session_summary_edit_page, route='/session-summaries/[session_id]/edit', title="Edit Session Summary", on_load=session_summary.SessionSummaryState.get_summary_detail)
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_ROUTE, title="Contact")
app.add_page(contact.contact_entries_list_page, route=navigation.routes.CONTACT_ENTRIES_ROUTE, title="Contact Entries", on_load = contact.ContactState.list_entries)
app.add_page(pages.getting_started_page, route=navigation.routes.GETTING_STARTED_ROUTE, title="Getting Started")
app.add_page(pages.rules_page, route=navigation.routes.RULES_ROUTE, title="Rules")
app.add_page(chatbot.chat_page, route=navigation.routes.CHAT_ROUTE, title="Chat")
app.add_page(
    character_sheet.character_sheet_content, 
    route="/character",
    title="Character Sheet | DM Assistant"
)

def debug_env():
    import os
    return rx.vstack(
        rx.text(f"CLIENT_ID set: {bool(os.getenv('GOOGLE_CLIENT_ID'))}"),
        rx.text(f"CLIENT_SECRET set: {bool(os.getenv('GOOGLE_CLIENT_SECRET'))}"),
        rx.text(f"REDIRECT_URI: {os.getenv('GOOGLE_REDIRECT_URI', 'NOT SET')}"),
    )

app.add_page(debug_env, route='/debug-env')