import reflex as rx
from datetime import datetime
from sqlmodel import Field, Relationship
import sqlalchemy as sa
from reflex_local_auth import LocalUser

from .. import utils

class UserInfo(rx.Model, table = True):

    email: str
    user_id: int = Field(foreign_key='localuser.id')
    user: LocalUser | None = Relationship()
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={'onupdate': sa.func.now(), "server_default": sa.func.now()},
        nullable=False,
    )