import reflex as rx

from . import routes

class NavState(rx.State):
    """The navigation state."""

    def to_login(self):
        return rx.redirect(routes.LOGIN_ROUTE)
    
    def to_logout(self):
        return rx.redirect(routes.LOGOUT_ROUTE)

    def to_session_add(self):
        """Navigate to the session add page."""
        return rx.redirect(routes.ADD_SESSION_SUMMARY_ROUTE)

    def to_session_summaries(self):
        """Navigate to the session summaries page."""
        return rx.redirect(routes.SESSION_SUMMARIES_ROUTE)
    
    def to_home(self):
        """Navigate to the home page."""
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about(self):
        """Navigate to the about page."""
        return rx.redirect(routes.ABOUT_ROUTE) 
    
    def to_files(self):
        """Navigate to the files page."""
        return rx.redirect(routes.FILES_ROUTE)
    
    def to_contact(self):
        """Navigate to the contact page."""
        return rx.redirect(routes.CONTACT_ROUTE)
    
    def to_chat(self):
        """Navigate to the chat page."""
        return rx.redirect(routes.CHAT_ROUTE)
    
    def to_getting_started(self):
        """Navigate to the getting started page."""
        return rx.redirect(routes.GETTING_STARTED_ROUTE)
    
    def to_rules(self):
        """Navigate to the rules page."""
        return rx.redirect(routes.RULES_ROUTE)
    