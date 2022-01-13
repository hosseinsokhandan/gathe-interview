from models.member import Member
from schemas.document import DocumentInSchema, DocumentSchema
from tortoise.query_utils import Q
from models.document import Document
from services.permission import permission_service
from fastapi.encoders import jsonable_encoder


class DocumentService:
    async def list_by_user(self, user_id: int):
        document_ids = await permission_service.list_user_documents_id(
            user_id, can_read=True
        )
        category_ids = await permission_service.list_user_categories_id(
            user_id, can_read=True
        )
        docs_qs = (
            await Document.filter(
                Q(id__in=document_ids) | Q(category_id__in=category_ids)
            )
            .select_related("category", "author")
            .distinct()
        )
        return docs_qs

    async def list_all(self):
        return await Document.all().prefetch_related("category", "author")
    
    async def get_document(self, document_id):
        return await Document.filter(id=document_id).prefetch_related(
            "category", "author"
        ).first()

    async def create(self, current_user: Member, document: DocumentInSchema):
        return await Document.create(
            author=current_user, category_id=document.category_id,
            subject=document.subject, content=document.content
        )

    async def update(
        self, document_id: int, document_in: DocumentSchema
    ):
        db_document: Document = await self.get_document(document_id)
        obj_data = jsonable_encoder(db_document)

        if isinstance(document_in, dict):
            update_data = document_in
        else:
            update_data = document_in.dict(exclude_unset=True)
        
        for field in obj_data:
            if field in update_data:
                setattr(db_document, field, update_data[field])

        return await db_document.save()



document_service = DocumentService()
