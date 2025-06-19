"""
Business rules for writing operations, uses repo
"""

from typing import List

from fastapi_pagination import Page, Params
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.apps.example.models import SomeModel
from backend.apps.example.repository import SomeModelRepo
from backend.apps.example.schemas import (
    SomeModelCreate,
    SomeModelDelete,
    SomeModelRead,
    SomeModelUpdate,
)
from backend.common.schemas.enums import OrderEnum


class SomeModelService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = SomeModelRepo(session=session)

    async def create_a_model(
        self,
        payload: SomeModelCreate,
    ) -> SomeModel:
        """
        Create model logic
        """
        return await self.repo.create(
            obj_in=payload,
        )

    async def bulk_create_a_model(
        self,
        payload: List[SomeModelCreate],
    ) -> List[SomeModelRead]:
        """
        Bulk Create model logic
        """
        return await self.repo.bulk_create(
            objs_in=payload,
        )

    async def list_some_models(
        self,
        params: Params,
        order: OrderEnum,
    ) -> Page[SomeModel]:
        return await self.repo.get_multi_paginated_ordered(
            params=params,
            order=order,
        )

    async def update_a_model(
        self,
        payload: SomeModelUpdate,
    ) -> SomeModelRead:
        """
        Create model logic
        """
        model = await self.repo.get(id=payload.id)
        return await self.repo.update(
            obj_current=model,
            obj_new=payload,
        )

    async def delete_a_model(self, payload: SomeModelDelete) -> SomeModelRead:
        """
        Delete model logic
        """
        return await self.repo.remove(
            id=payload.id,
        )
