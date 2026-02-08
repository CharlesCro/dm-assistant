"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


from rxconfig import config

from .ui.base import base_page
from .auth.state import GoogleState
from . import  auth, session_summary, contact, navigation, pages, chatbot, character_sheet


import reflex as rx
from reflex_google_auth import (
    GoogleAuthState,
    require_google_login,
)

from .services.adk_service import initialize_adk, run_adk_sync
from .config.settings import MESSAGE_HISTORY_KEY, get_api_key

# --- Initiate ADK ---
# Assuming 'initialize_adk' and 'run_adk_sync' handle the core logic
adk_runner, current_session_id = initialize_adk()

@require_google_login()
def index() -> rx.Component:
    
      # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Welcome to Dungeon Master Assistant!", weight="bold"),
            rx.text(
                "Dungeoon Master Assistant is an AI-powered tool designed to help Dungeon Masters create and manage their Dungeons & Dragons campaigns with ease.",
                size="5",
            ),
            rx.link(
                rx.button("Get Started", size="3", color_scheme="teal"),
                href=navigation.routes.GETTING_STARTED_ROUTE,
                is_external=True,
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
   
  
    
import dm_assistant.styles as styles

app = rx.App(
    
    theme=styles.base_theme,
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEET,
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