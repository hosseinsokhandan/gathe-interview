from typing import Optional
from pydantic import BaseModel
from schemas.category import CategorySchema
from schemas.member import MemberSchema


class DocumentSchema(BaseModel):
    id: int
    category: Optional[CategorySchema] = None
    author: Optional[MemberSchema] = None

    class Config:
        orm_mode = True
