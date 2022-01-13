from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from deps import is_admin, get_current_user
from models.document import Document
from schemas.permission import PermissionDocumentSchema
from services.permission import permission_service
from services.document import document_service
from schemas.document import DocumentSchema, DocumentInSchema
from models.member import Member

router = APIRouter()


@router.get("/", response_model=List[DocumentSchema])
async def list_documents(
    current_user: Member = Depends(get_current_user),
    is_admin: bool = Depends(is_admin),
):
    if is_admin:
        return await document_service.list_all()
    docs = await document_service.list_by_user(current_user.id)
    return docs


@router.post("/", response_model=DocumentSchema)
async def create_document(
    document: DocumentInSchema,
    current_user: Member = Depends(get_current_user),
):
    if await permission_service.check_create_permission(
        current_user, document.category_id
    ):
        document = await document_service.create(
            current_user, document
        )
        
        return await document.fetch_related()
    
    raise HTTPException(status_code=403, detail="Forbidden")


@router.get("/{document_id}", response_model=DocumentSchema)
async def get_document(
    document_id: int,
    current_user: Member = Depends(get_current_user),
):
    if await permission_service.check_permission(
        current_user, document_id, "can_read"
    ):
        return await document_service.get_document(document_id)
    raise HTTPException(status_code=403, detail="Forbidden")



@router.put("/{document_id}", response_model=DocumentSchema)
async def get_document(
    document_id: int,
    document: DocumentInSchema,
    current_user: Member = Depends(get_current_user),
):
    if await permission_service.check_permission(
        current_user, document_id, "can_read"
    ):
        return await document_service.update(document_id, document)
    raise HTTPException(status_code=403, detail="Forbidden")