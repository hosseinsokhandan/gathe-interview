from typing import List
from fastapi import APIRouter
from fastapi.param_functions import Depends
from deps import is_admin, get_current_user
from models.document import Document
from services.document import document_service
from schemas.document import DocumentSchema
from models.member import Member

router = APIRouter()


@router.get("/", response_model=List[DocumentSchema])
async def list_user_docs(
    current_user: Member = Depends(get_current_user),
    is_admin: bool = Depends(is_admin),
):
    if is_admin:
        return await document_service.list_all()
    docs = await document_service.list_by_user(current_user.id)
    return docs
