import reflex as rx

from ..ui.base import base_page

def about_page() -> rx.Component:
    """About Page."""
    PRIVACY_POLICY_TEXT = """
    # Privacy Policy for DM Assistant
    **Effective Date:** February 7, 2026

    At **DM Assistant**, we respect your privacy and are committed to protecting the personal data you share with us.

    ### 1. Information We Collect
    We only collect information necessary to provide you with a functional experience:
    * **Account Information:** We receive your name and email address via Google Authentication.
    * **User-Generated Content:** We store the chat messages, campaign data, and prompts you enter.
    * **Technical Data:** Basic log info (IP address, browser type) is collected via Reflex hosting for performance monitoring.

    ### 2. How We Use Your Information
    We use your data to identify you, save your campaign history, and generate AI responses. **We do not sell your personal data.**

    ### 3. Third-Party Services
    * **Google Cloud Vertex AI:** Your inputs are sent to Vertex AI for processing. Google does not use this data to train their foundational models under their Enterprise privacy terms.
    * **Google Authentication:** Manages logins subject to [Google’s Privacy Policy](https://policies.google.com/privacy).
    * **Reflex Hosting:** Provides the secure infrastructure for our database.

    ### 4. Cookies and Local Storage
    We use session cookies and local storage to keep you logged in. Disabling these may cause the app to malfunction.

    ### 5. Data Deletion
    You may request the deletion of your account and data at any time by emailing **charlescrocicchia@gmail.com**.
    """

    TOS_TEXT = """
    # Terms of Service for DM Assistant
    **Last Updated:** February 7, 2026

    ### 1. Description of Service
    DM Assistant is an AI-powered tool for campaign management. By using this service, you agree to these terms.

    ### 2. User Content & AI Accuracy
    * **Ownership:** You own your prompts; you are granted rights to the AI output.
    * **AI Limitations:** You acknowledge that AI can provide inaccurate or "hallucinated" information. The Dungeon Master is the final arbiter of all game rules and content.

    ### 3. Prohibited Conduct
    You agree not to use the service for illegal acts, hate speech, or attempting to reverse-engineer the AI or hosting infrastructure.

    ### 4. Disclaimer of Warranties
    **DM Assistant is provided "AS IS."** We make no warranties regarding the accuracy or availability of the service.

    ### 5. Limitation of Liability
    Charles Crocicchia and DM Assistant shall not be liable for any damages, including loss of data or campaign-breaking AI errors, arising from your use of the service.

    ### 6. Contact
    For legal inquiries: **charlescrocicchia@gmail.com**
    """
    about_child = rx.vstack(
        rx.heading("About Dungeon Master Assistant", weight="bold"),
        rx.text(
            "Dungeon Master Assistant is an AI-powered tool designed to help Dungeon Masters create and manage their Dungeons & Dragons campaigns with ease.",
            size="5",
        ),
        rx.text(
            "With features like automated story generation, NPC creation, and encounter balancing, Dungeon Master Assistant aims to streamline the campaign creation process and enhance the gaming experience for both DMs and players.",
            size="5",
        ),
        rx.divider(),
        rx.vstack(
        rx.heading("Legal Information", size="8", margin_bottom="1em"),
        
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Privacy Policy", value="privacy"),
                rx.tabs.trigger("Terms of Service", value="tos"),
            ),
            rx.tabs.content(
                rx.box(
                    rx.markdown(PRIVACY_POLICY_TEXT),
                    padding="2em",
                    border="1px solid #e5e7eb",
                    border_radius="8px",
                    margin_top="1em",
                ),
                value="privacy",
            ),
            rx.tabs.content(
                rx.box(
                    rx.markdown(TOS_TEXT),
                    padding="2em",
                    border="1px solid #e5e7eb",
                    border_radius="8px",
                    margin_top="1em",
                ),
                value="tos",
            ),
            width="100%",
        ),
        max_width="800px",
        margin="auto",
        padding="2em",
    ),
        spacing="5",
        justify="center",
        text_align="center",
        align="center",
        min_height="85vh",
        id='about-child'
    )
    return base_page(
        about_child
    )