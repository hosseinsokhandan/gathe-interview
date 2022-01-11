from typing import Optional
from pydantic import BaseModel, validator


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
