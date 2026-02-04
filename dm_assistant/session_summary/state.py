import reflex as rx
from typing import Optional, List

from .model import SessionSummaryModel

from sqlmodel import select


class SessionSummaryState(rx.State):
    summaries: List['SessionSummaryModel'] = []
    summary: Optional['SessionSummaryModel'] = None

    @rx.var
    def session_summary_id(self) -> str:
        print(self.router.page.params)
        return self.router.page.params.get('session_id', "")
    
    def get_summary_detail(self):
        with rx.session() as session:
            if self.session_summary_id == '':
                self.summary = None
                return 
            result = session.exec(
                select(SessionSummaryModel).where(
                    SessionSummaryModel.id == self.session_summary_id
                )
            ).one_or_none()

            self.summary = result

    
    def add_summary(self, form_data: dict):
        with rx.session() as session:
            summary = SessionSummaryModel(**form_data)
            print('Adding', summary)
            session.add(summary)
            session.commit()
            session.refresh(summary)

            self.summary = summary

    def load_summaries(self):
        with rx.session() as session:
            result = session.exec(
                select(SessionSummaryModel)
            ).all()

            self.summaries = result

    # def get_summary(self, session_id: int):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(SessionSummaryModel)
    #         ).all()

    #         self.summaries = result


    
class SessionAddSummaryFormState(SessionSummaryState):

    form_data: dict = {}


    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.add_summary(form_data)