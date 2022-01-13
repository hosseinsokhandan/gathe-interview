from httpx import AsyncClient
from main import app
import pytest

from models.permission import CategoryPermission
from tests.helpers import create_permission_helper


@pytest.mark.asyncio
async def test_get_docuement_non_admin(provide_test_data, non_admin_header: dict):
    """In this test I try to create permission with a non-admin account"""
    await create_permission_helper(
        model=CategoryPermission,
        user=2,
        category_id=2,
        can_create=False,
        can_update=False,
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/", headers=non_admin_header)
        print(response.json())
