from httpx import AsyncClient
from main import app
import pytest


@pytest.mark.asyncio
async def test_set_permission_api_error_403(provide_test_data, non_admin_header: dict):
    """In this test I try to create permission with a non-admin account"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("permission/create", json={}, headers=non_admin_header)
        assert response.status_code == 403


@pytest.mark.asyncio
async def test_set_permission_api_error_401(provide_test_data):
    """In this test I try to create permission without providing username header"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("permission/create", json={}, headers={})
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_set_category_permission_api(provide_test_data, admin_header: dict):
    """In this test I try to set permission based on category"""
    data = {
        "category_id": 1,
        "member_id": 2,
        "can_create": False,
        "can_read": True,
        "can_update": True,
        "can_delete": False,
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("permission/create", json=data, headers=admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_set_category_permission_api(provide_test_data, admin_header: dict):
    """In this test I try to set permission based on category"""
    data = {
        "document_id": 1,
        "member_id": 3,
        "can_create": False,
        "can_read": True,
        "can_update": True,
        "can_delete": False,
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("permission/create", json=data, headers=admin_header)
        assert response.status_code == 200
