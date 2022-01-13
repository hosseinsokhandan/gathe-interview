from typing import Any, Optional, Union
from pydantic import BaseModel, validator, Field


class PermissionInSchema(BaseModel):
    member_id: int
    can_create: bool
    can_read: bool
    can_update: bool
    can_delete: bool

    document_id: Optional[int] = None
    category_id: Optional[int] = None

    @validator("category_id")
    def check_atleast_one_exist(cls, v, values, **kwargs):
        document_id = values.get("document_id")
        category_id = v
        if not document_id and not category_id:
            raise ValueError("Either document_id or category_id is required.")
        if document_id and category_id:
            raise ValueError("document_id or category_id, not both.")
        return v


class PermissionOutSchema(BaseModel):
    member_id: int
    can_create: bool
    can_read: bool
    can_update: bool
    can_delete: bool

    document_id: Optional[int] = None
    category_id: Optional[int] = None

class PermissionDocumentSchema(BaseModel):
    id: int
    can_create: bool
    can_read: bool
    can_update: bool
    can_delete: bool
    author: Union[dict, int] = None
    category: Union[dict, int] = None

    class Config:
        orm_mode = True
    