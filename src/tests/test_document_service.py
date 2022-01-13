from models.permission import CategoryPermission, DocumentPermission
from services.document import document_service
from tests.helpers import create_permission_helper
import pytest


@pytest.mark.asyncio
async def test_list_document_test_document_direct_permission(provide_test_data):
    # category 2 has 3 documents ids => [2,3,4]
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
    documents = await document_service.list_by_user(3)
    assert [1, 2] == [doc.id for doc in documents]


@pytest.mark.asyncio
async def test_list_document_by_category_permission(provide_test_data):
    # category 2 has 3 documents ids => [2,3,4]
    await create_permission_helper(
        model=CategoryPermission,
        user=3,
        category_id=2,
        can_create=False,
        can_update=False,
    )
    documents = await document_service.list_by_user(3)
    assert [2, 3, 4] == [doc.id for doc in documents]
