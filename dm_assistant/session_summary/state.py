from datetime import datetime
import reflex as rx
from typing import Optional, List

from .model import SessionSummaryModel

from sqlmodel import select


from .. import navigation

SESSION_SUMMARIES_ROUTE = navigation.routes.SESSION_SUMMARIES_ROUTE
if SESSION_SUMMARIES_ROUTE.endswith('/'):
    SESSION_SUMMARIES_ROUTE = SESSION_SUMMARIES_ROUTE[:-1]


class SessionSummaryState(rx.State):
    summaries: List['SessionSummaryModel'] = []
    summary: Optional['SessionSummaryModel'] = None
    summary_text: str = ""
    summary_publish_active: bool = False

    @rx.var
    def session_summary_url(self) -> str:
        if not self.summary:
            return f'{SESSION_SUMMARIES_ROUTE}'
        return f'{SESSION_SUMMARIES_ROUTE}/{self.summary.id}'
    
    
    @rx.var
    def session_summary_edit_url(self) -> str:
        if not self.summary:
            return f'{SESSION_SUMMARIES_ROUTE}'
        return f'{SESSION_SUMMARIES_ROUTE}/{self.summary.id}/edit'


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
                    (SessionSummaryModel.id == self.session_summary_id) &
                    ( SessionSummaryModel.publish_active == True)
                )
            ).one_or_none()

            self.summary = result
            if result is None:
                self.summary_text = ""
                return
            self.summary_text = result.summary_text
            self.summary_publish_active = result.publish_active

    
    def add_summary(self, form_data: dict):
        with rx.session() as session:
            summary = SessionSummaryModel(**form_data)
            print('Adding', summary)
            session.add(summary)
            session.commit()
            session.refresh(summary)

            self.summary = summary

    def edit_summary(self, summary_id: int, updated_data: dict):
        with rx.session() as session:
            result = session.exec(
                select(SessionSummaryModel).where(
                    SessionSummaryModel.id == summary_id
                )
            ).one_or_none()

            if result == None:
                return
            
            for key, value in updated_data.items():
                setattr(result, key, value)
            session.add(result)
            session.commit()
            session.refresh(result)

            self.summary = result

    def load_summaries(self, published_only: bool = True):
        lookup_args = ()
        if published_only:
            lookup_args = (
                   ( SessionSummaryModel.publish_active == True) &
                     ( SessionSummaryModel.publish_date <= datetime.utcnow())
                )

        with rx.session() as session:
            result = session.exec(
                select(SessionSummaryModel).where(
                   *lookup_args
                )
            ).all()

            self.summaries = result


    def to_session_summary(self, edit_page = False):
        if not self.summary:
            return rx.redirect(SESSION_SUMMARIES_ROUTE)
        
        if edit_page:
            return rx.redirect(f'{SESSION_SUMMARIES_ROUTE}/{self.summary.id}/edit')
        return rx.redirect(f'{SESSION_SUMMARIES_ROUTE}/{self.summary.id}')
    
class SessionAddSummaryFormState(SessionSummaryState):

    form_data: dict = {}


    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.add_summary(form_data)
        return self.to_session_summary(edit_page=True)


    
class SessionEditSummaryFormState(SessionSummaryState):

    form_data: dict = {}
    # summary_text: str = ""


    @rx.var
    def publish_display_date(self) -> str:
        if not self.summary:
            return datetime.now().strftime('%Y-%m-%d')
        
        if not self.summary.publish_date:
            return datetime.now().strftime('%Y-%m-%d')
        
        return self.summary.publish_date.strftime('%Y-%m-%d')
    
    @rx.var
    def publish_display_time(self) -> str:
        if not self.summary:
            return datetime.now().strftime('%H:%M:%S') 
        if not self.summary.publish_date:
            return datetime.now().strftime('%H:%M:%S')
        return datetime.now().strftime('%H:%M:%S')


    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        session_id = form_data.pop('session_id', None)
        publish_date = form_data.pop('publish_date', None)
        publish_time = form_data.pop('publish_time', None)
        print('Publish Date:', publish_date)
        print('Publish Time:', publish_time)
        publish_input_string = f'{publish_date} {publish_time}'
        final_publish_date = None

        try:
            final_publish_date = datetime.strptime(publish_input_string, '%Y-%m-%d %H:%M:%S')
        except:
            final_publish_date = None
        publish_active = False
        if 'publish_active' in form_data:
            publish_active = form_data.pop('publish_active') == 'on'
        updated_data = {**form_data}
        updated_data['publish_active'] = publish_active
        updated_data['publish_date'] = final_publish_date
        print(session_id, updated_data)
        self.edit_summary(session_id, updated_data)
        return self.to_session_summary()