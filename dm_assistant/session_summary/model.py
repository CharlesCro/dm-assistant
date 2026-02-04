import reflex as rx
from datetime import datetime
from sqlmodel import Field
import sqlalchemy as sa

from .. import utils

class SessionSummaryModel(rx.Model, table = True):

    """Model for storing session summaries."""

    title: str
    summary_text: str 
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