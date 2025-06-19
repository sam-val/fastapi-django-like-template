"""
# Low-level DB access functions
"""

from sqlmodel import col, select
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.apps.example.models import SomeModel
from backend.apps.example.schemas import SomeModelCreate, SomeModelUpdate
from backend.common.repository.base import CRUDBase


class SomeModelRepo(CRUDBase[SomeModel, SomeModelCreate, SomeModelUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(SomeModel, session=session)

    async def get_some_models_by_name(
        self, *, name: str, db_session: AsyncSession | None = None
    ) -> SomeModel:
        db_session = db_session or self.session
        some_model = await db_session.exec(
            select(SomeModel).where(col(SomeModel.name).ilike(f"%{name}%"))
        )
        return some_model.all()
