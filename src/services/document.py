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
        return (
            await Document.filter(
                Q(id__in=document_ids) | Q(category_id__in=category_ids)
            )
            .prefetch_related("category", "author")
            .distinct()
        )

    async def list_all(self):
        return await Document.all().prefetch_related("category", "author")


document_service = DocumentService()
