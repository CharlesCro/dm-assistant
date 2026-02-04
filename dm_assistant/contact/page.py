import reflex as rx

from ..ui.base import base_page

from . import form, state, model

def contact_entry_list_item(contact: model.ContactEntryModel) -> rx.Component:
    """Create a contact entry list item."""
    return rx.box(
        rx.vstack(
            rx.heading(contact.name, size="4", weight="bold"),
            rx.text(f"Email: {contact.email}", size="2"),
            rx.text(f"Message: {contact.message}", size="2"),
            spacing="2",
        ),
        border="1px solid",
        border_color="gray.300",
        padding="4",
        border_radius="md",
        width="100%",
        max_width="600px",
    )


def contact_entries_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size = '5', weight="bold"),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
            id='contact-child'
        )
    )

def contact_page() -> rx.Component:
    """Contact Page."""
    

    contact_child = rx.vstack(
        rx.heading("Contact Us", weight="bold"),
        rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
        form.contact_form(),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id='contact-child'
    )
    return base_page(
        contact_child
    )