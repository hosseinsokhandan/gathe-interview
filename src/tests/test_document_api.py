from httpx import AsyncClient
from main import app
import pytest

from models.permission import CategoryPermission, DocumentPermission
from tests.helpers import create_permission_helper


@pytest.mark.asyncio
async def test_list_docuement_non_admin(provide_test_data, non_admin_header: dict):
    await create_permission_helper(
        model=DocumentPermission,
        user=2,
        document_id=2,
        can_create=False,
        can_update=False,
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/", headers=non_admin_header)
        assert response.json()[0]["id"] == 2


@pytest.mark.asyncio
async def test_list_docuement_admin(provide_test_data, admin_header: dict):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/", headers=admin_header)
        assert len(response.json()) == 4 # we create 4 document in conftest file



@pytest.mark.asyncio
async def test_get_docuement(provide_test_data, non_admin_header: dict):
    await create_permission_helper(
        model=DocumentPermission,
        user=2,
        document_id=3,
        can_create=False,
        can_update=False,
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/3", headers=non_admin_header)
        assert response.json()["id"] == 3
        

@pytest.mark.asyncio
async def test_get_docuement_with_category_permission(provide_test_data, non_admin_header: dict):
    await create_permission_helper(
        model=CategoryPermission,
        user=2,
        category_id=1,
        can_create=False,
        can_update=False,
        can_delete=False,
    )
    await create_permission_helper(
        model=DocumentPermission,
        user=2,
        document_id=3,
        can_read=True,
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/4", headers=non_admin_header)
        assert response.status_code == 403

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/3", headers=non_admin_header)
        assert response.json()["id"] == 3

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/2", headers=non_admin_header)
        assert response.status_code == 403

    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/1", headers=non_admin_header)
        assert response.json()["id"] == 1



@pytest.mark.asyncio
async def test_get_docuement_with_category_permission_admin(provide_test_data, admin_header: dict):

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/4", headers=admin_header)
        assert response.json()["id"] == 4

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/3", headers=admin_header)
        assert response.json()["id"] == 3

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/2", headers=admin_header)
        assert response.json()["id"] == 2

    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("document/1", headers=admin_header)
        assert response.json()["id"] == 1



@pytest.mark.asyncio
async def test_create_document_with_non_admin_user(provide_test_data, non_admin_header: dict):
    await create_permission_helper(
        model=CategoryPermission,
        user=2,
        category_id=1,
        can_create=True,
        can_update=False,
        can_delete=False,
    )
    data = {
        "subject": "1",
        "content": "1",
        "category_id": 1
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("document/", json=data, headers=non_admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_document_with_admin_user(provide_test_data, admin_header: dict):

    data = {
        "subject": "1",
        "content": "1",
        "category_id": 1
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("document/", json=data, headers=admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_document_with_non_admin_user(provide_test_data, non_admin_header: dict):
    await create_permission_helper(
        model=CategoryPermission,
        user=2,
        category_id=1,
        can_create=True,
        can_update=True,
        can_delete=False,
    )
    data = {
        "subject": "Subject 1 --> 11",
        "content": "Content 1 --> 11",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("document/1", json=data, headers=non_admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_document_with_admin_user(provide_test_data, admin_header: dict):
    data = {
        "subject": "Subject 1 --> 11",
        "content": "Content 1 --> 11",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("document/3", json=data, headers=admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_document_with_non_admin_user(provide_test_data, admin_header: dict):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("document/1", headers=admin_header)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_document_with_non_admin_user(provide_test_data, non_admin_header: dict):

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("document/3", headers=non_admin_header)
        assert response.status_code == 403

    await create_permission_helper(
        model=DocumentPermission,
        user=2,
        document_id=3,
        can_delete=True
    )

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("document/3", headers=non_admin_header)
        assert response.status_code == 200