from models.permission import CategoryPermission, DocumentPermission
from schemas.permission import PermissionInSchema
from services.permission import permission_service
import pytest

from tests.helpers import create_permission_helper


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


@pytest.mark.asyncio
async def test_permission_list_user_categories_id(provide_test_data):
    """give me list of categories that user 3 has access to"""
    await create_permission_helper(
        model=CategoryPermission, user=3, category_id=1, can_create=False
    )
    await create_permission_helper(
        model=CategoryPermission,
        user=3,
        category_id=2,
        can_update=False,
        can_delete=False,
        can_create=False,
    )
    await create_permission_helper(
        model=CategoryPermission,
        user=3,
        category_id=3,
        can_read=False,
        can_delete=False,
        can_create=False,
    )

    read_categories = await permission_service.list_user_categories_id(
        member_id=3, can_read=True
    )
    update_categories = await permission_service.list_user_categories_id(
        member_id=3, can_update=True
    )
    create_categories = await permission_service.list_user_categories_id(
        member_id=3, can_create=True
    )

    assert read_categories == [1, 2]
    assert update_categories == [1, 3]
    assert create_categories == []


@pytest.mark.asyncio
async def test_permission_list_user_documents_id(provide_test_data):
    """give me list of documents that user 3 has access to"""
    await create_permission_helper(
        model=DocumentPermission,
        user=3,
        document_id=1,
        can_create=False,
        can_update=False,
    )
    await create_permission_helper(
        model=DocumentPermission,
        user=3,
        document_id=2,
        can_update=False,
        can_delete=False,
    )
    await create_permission_helper(
        model=DocumentPermission,
        user=3,
        document_id=3,
        can_read=False,
        can_delete=False,
        can_create=False,
    )

    read_documents = await permission_service.list_user_documents_id(
        member_id=3, can_read=True
    )
    update_documents = await permission_service.list_user_documents_id(
        member_id=3, can_update=True
    )
    create_documents = await permission_service.list_user_documents_id(
        member_id=3, can_create=True
    )
    delete_documents = await permission_service.list_user_documents_id(
        member_id=3, can_delete=True
    )

    assert read_documents == [1, 2]
    assert update_documents == [3]
    assert create_documents == [2]
    assert delete_documents == [1]
