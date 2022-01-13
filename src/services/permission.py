from models.member import Member
from models.permission import CategoryPermission, DocumentPermission
from schemas.permission import PermissionInSchema
from utils import is_admin


class PermissionService:
    async def set_permission(self, permission_data: PermissionInSchema):
        if permission_data.document_id:
            return await self.__set_document_permission(permission_data)
        else:
            return await self.__set_category_permission(permission_data)

    async def __set_category_permission(self, permission_data: PermissionInSchema):
        return await CategoryPermission.create(**permission_data.dict())

    async def __set_document_permission(self, permission_data: PermissionInSchema):
        return await DocumentPermission.create(**permission_data.dict())

    async def list_user_categories_id(self, member_id: int, **kwargs):
        return await CategoryPermission.filter(
            member_id=member_id, **kwargs
        ).values_list("category_id", flat=True)

    async def list_user_documents_id(self, member_id: int, **kwargs):
        return await DocumentPermission.filter(
            member_id=member_id, **kwargs
        ).values_list("document_id", flat=True)


    async def get_doc_permission(self, user_id, doc_id):
        return await DocumentPermission.filter(document_id=doc_id, member_id=user_id).first()
    
    async def get_cat_permission(self, user_id, cat_id):
        return await CategoryPermission.filter(category_id=cat_id, member_id=user_id).first()

    async def check_permission(
        self, current_user: Member, document_id: int, can_name: str
    ):
        if is_admin(current_user):
            return True

        doc_perm = await self.get_doc_permission(current_user.id, document_id)
        if doc_perm and getattr(doc_perm, can_name, False):
            return True

        from services.document import document_service
        document = await document_service.get_document(document_id)
        cat_perm = await self.get_cat_permission(current_user.id, document.category_id)
        if cat_perm and getattr(cat_perm, can_name, False):
            return True

        return False

    async def check_create_permission(
        self, current_user: Member, category_id: int
    ):
        if is_admin(current_user):
            return True

        cat_perm = await self.get_cat_permission(current_user.id, category_id)
        if cat_perm and cat_perm.can_create:
            return True
        return False

permission_service = PermissionService()
