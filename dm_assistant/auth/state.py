import reflex as rx
import reflex_local_auth

import sqlmodel
from typing import Optional

from .models import UserInfo


class SessionState(reflex_local_auth.LocalAuthState):
    @rx.var(cache=True)
    def authenticated_user_info(self) -> UserInfo | None:
        if self.authenticated_user.id < 0:
            return None
        with rx.session() as session:
            result = session.exec(
                sqlmodel.select(UserInfo).where(
                    UserInfo.user_id == self.authenticated_user.id
                ),
            ).one_or_none()
            if result is None:
                return None
            print("Did we make it here?", result.user)
            return result
        
    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        
        print(self.authenticated_user_info)


    def perform_logout(self):

        self.do_logout()

        return rx.redirect('/')


class MyRegisterState(reflex_local_auth.RegistrationState):
    # This event handler must be named something besides `handle_registration`!!!
    def handle_registration_email(self, form_data):
        registration_result = self.handle_registration(form_data)
        if self.new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
        return registration_result