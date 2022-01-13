from models.permission import CategoryPermission, DocumentPermission
from schemas.permission import PermissionInSchema


class PermissionService:
    async def set_permission(self, permission_data: PermissionInSchema):
        if permission_data.document_id:
            return await self.__set_document_permission(permission_data)
        else:
            return await self.__set_category_permission(permission_data)

    async def __set_category_permission(self, permission_data: PermissionInSchema):
        return await CategoryPermission.create(
            member_id=permission_data.member_id,
            category_id=permission_data.category_id,
            can_read=permission_data.can_read,
            can_update=permission_data.can_update,
            can_delete=permission_data.can_delete,
            can_create=permission_data.can_create,
        )

    async def __set_document_permission(self, permission_data: PermissionInSchema):
        return await DocumentPermission.create(
            member_id=permission_data.member_id,
            document_id=permission_data.document_id,
            can_read=permission_data.can_read,
            can_update=permission_data.can_update,
            can_delete=permission_data.can_delete,
            can_create=permission_data.can_create,
        )


permission_service = PermissionService()