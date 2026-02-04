from datetime import datetime, timezone

import reflex as rx

from sqlmodel import Field
import sqlalchemy as sa

from .. import utils

class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    name: str = Field(nullable = True)
    email: str = Field(nullable = True)
    message: str = Field(nullable = True)
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )

