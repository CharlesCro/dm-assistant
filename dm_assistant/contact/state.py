import reflex as rx
import asyncio

from sqlmodel import select
from typing import List

from .model import ContactEntryModel


class ContactState(rx.State):


    entries: list[ContactEntryModel] = []    
    form_data: dict = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self) -> str:
        name = self.form_data.get('name', 'Guest')
        return f'Thank you {name}!'

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data

        with rx.session() as session:
            db_entry = ContactEntryModel(
                **form_data
            )
            session.add(db_entry)
            session.commit()

            self.did_submit = True
            yield

        await asyncio.sleep(2)
        self.did_submit = False
        yield


    def list_entries(self):

        with rx.session() as session:
            entries = session.exec(select(ContactEntryModel)).all()
            print(entries)
            self.entries = entries
