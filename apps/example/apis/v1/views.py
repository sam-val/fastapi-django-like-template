from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status
from fastapi_pagination import Page, Params
from sqlmodel.ext.asyncio.session import AsyncSession

from apps.example.schemas import (
    SomeModelCreate,
    SomeModelDelete,
    SomeModelRead,
    SomeModelUpdate,
)
from apps.example.services.core_service import SomeModelService
from common.schemas.enums import OrderEnum
from common.schemas.response import StandardResponse
from config.db import get_session

router = APIRouter()


@router.post(
    "/model",
    response_model=StandardResponse[SomeModelRead],
    status_code=status.HTTP_201_CREATED,
)
async def create_model_api(
    payload: SomeModelCreate,
    session: AsyncSession = Depends(get_session),
):
    service = SomeModelService(session=session)
    model = await service.create_a_model(
        payload=payload,
    )
    return StandardResponse(
        data=model,
    )


@router.post(
    "/models",
    response_model=StandardResponse[List[SomeModelRead]],
    status_code=status.HTTP_201_CREATED,
)
async def bulk_create_model_api(
    payload: List[SomeModelCreate],
    session: AsyncSession = Depends(get_session),
):
    service = SomeModelService(session=session)
    model = await service.bulk_create_a_model(
        payload=payload,
    )
    return StandardResponse(
        data=model,
    )


@router.get(
    "/models",
    response_model=StandardResponse[Page[SomeModelRead]],
    status_code=status.HTTP_200_OK,
)
async def get_models_api(
    order: Optional[OrderEnum] = Query(
        default=OrderEnum.asc,
        description="Optional",
    ),
    params: Params = Depends(),  # load page&size into params
    session: AsyncSession = Depends(get_session),
):
    service = SomeModelService(session=session)
    paginated_models = await service.list_some_models(
        params=params,
        order=order,
    )
    return StandardResponse(
        data=paginated_models,
    )


@router.put(
    "/model",
    response_model=StandardResponse[SomeModelRead],
    status_code=status.HTTP_200_OK,
)
async def update_a_model_api(
    payload: SomeModelUpdate,
    session: AsyncSession = Depends(get_session),
):
    service = SomeModelService(session=session)
    updated_model = await service.update_a_model(
        payload=payload,
    )
    return StandardResponse(
        data=updated_model,
    )


@router.delete(
    "/model",
    response_model=StandardResponse[SomeModelRead],
    status_code=status.HTTP_200_OK,
)
async def delete_a_model_api(
    payload: SomeModelDelete,
    session: AsyncSession = Depends(get_session),
):
    service = SomeModelService(session=session)
    updated_model = await service.delete_a_model(
        payload=payload,
    )
    return StandardResponse(data=updated_model, message="Delete success")
