from typing import Optional

from sqlmodel import Field, SQLModel

from backend.common.mixins.models import TimestampMixin


class SomeModel(SQLModel, TimestampMixin, table=True):
    """
    Model example
    """

    # __table_args__ = {"schema": "your_schema"}

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
