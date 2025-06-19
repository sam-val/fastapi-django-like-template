# schemas.py
from typing import Optional

from pydantic import BaseModel, Field


class SomeModelCreate(BaseModel):
    name: str = Field(..., min_length=1)


class SomeModelUpdate(BaseModel):
    id: int = Field(..., ge=1)
    name: Optional[str] = None


class SomeModelDelete(BaseModel):
    id: int = Field(..., ge=1)


class SomeModelRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # For SQLModel compatibility
