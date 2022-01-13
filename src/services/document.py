from models.member import Member
from schemas.document import DocumentInSchema, DocumentInUpdateSchema
from tortoise.query_utils import Q
from models.document import Document
from services.permission import permission_service


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
        return await Document.get(id=document_id).prefetch_related(
            "category", "author"
        ).first()

    async def create(self, current_user: Member, document: DocumentInSchema):
        return await Document.create(author=current_user, **document.dict())

    async def update(
        self, document_id: int, document: DocumentInUpdateSchema
    ):
        await Document.filter(id=document_id).update(**document.dict())
        return await self.get_document(document_id)

    async def delete_document(self, document_id: int):
        await Document.filter(id=document_id).delete()



document_service = DocumentService()
