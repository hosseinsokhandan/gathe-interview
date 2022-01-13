from typing import Optional, Dict, Any
from pydantic import BaseModel, ValidationError, validator
from schemas.category import CategorySchema
from schemas.member import MemberSchema
from services.permission import permission_service


class DocumentSchema(BaseModel):
    id: int
    category: Optional[CategorySchema] = None
    author: Optional[MemberSchema] = None


    class Config:
        orm_mode = True


class DocumentInSchema(BaseModel):
    category_id: int
    subject: str
    content: str