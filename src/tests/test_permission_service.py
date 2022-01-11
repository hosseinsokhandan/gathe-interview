from models.permission import CategoryPermission, DocumentPermission
from schemas.permission import PermissionInSchema
from services.permission import permission_service
import pytest


@pytest.mark.asyncio
async def test_category_permission(provide_test_data):
    data = PermissionInSchema(
        member_id=1,
        category_id=1,
        can_create=True,
        can_delete=False,
        can_read=True,
        can_update=False,
    )
    resp = await permission_service.set_permission(data)
    assert resp.member_id == 1
    assert resp.__class__ == CategoryPermission


@pytest.mark.asyncio
async def test_document_permission(provide_test_data):
    data = PermissionInSchema(
        member_id=2,
        document_id=2,
        can_create=False,
        can_delete=True,
        can_read=False,
        can_update=True,
    )
    resp = await permission_service.set_permission(data)
    assert resp.member_id == 2
    assert resp.__class__ == DocumentPermission
