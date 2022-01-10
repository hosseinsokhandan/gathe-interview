# Document Permission System

We want to implement a system that manages the documents of a company.
In this system members can access or modify the documents based on their permissions.

## APIs

Members can do CRUD operations based on their permissions and documents using APIs.

## Member

Members should have `username` and an unique `id`.
**Default member should be `admin`.**

**Note**: We skip authorization in this system and only validate users by `username` that exists in the requets `headers`.

## Document

Documents should have `author`, `category`, `subject`, and `content`.

### Category

Categories should have only `name`.

## Permission

Permissions include `create`, `read`, `update` and `delete`.

Only `admin` member can set permission for other memebers to access or modify a specific document or the documents of a category.

## Category Permission

The `admin` can set permissions for a category and the permission will apply to all documents related to the category.

For example the member `John`, could `create` and `read` all documents in the category `Report`.

## Document Permission

Also admin can set permission a specific document in the category and the permission will only apply to that document.

For example the member `Alice` could `read` all documents in the category `Outcomes` but only could `update`
the document with id `3`.

## Dependencies

- Python 3.9 or later.
- FastAPI
- Tortoise-ORM.

## Initial Project Setup

1. Install [Poetry](https://python-poetry.org/)
2. Run `poetry install && poetry shell`

## Test Case Examples

### Set Category Permission

Request url: <http://localhost:8000/permission/create/>

Request data example:

```json
{
    "category_id": 1,
    "member_id": 2,
    "can_create": false,
    "can_read": true,
    "can_update": true,
    "can_delete": false
}
```

### Set Document Permission

Request url: <http://localhost:8000/permission/create/>

Request data example:

```json
{
    "document_id": 1,
    "member_id": 3,
    "can_create": false,
    "can_read": true,
    "can_update": true,
    "can_delete": false
}
```

## Get Documents

Request url: <http://localhost:8000/document/>

Response example:

```json
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Report"
        },
        "author": {
            "id": 2,
            "username": "john"
        },
        "can_create": false,
        "can_read": true,
        "can_update": true,
        "can_delete": false
    },
    {
        "id": 2,
        "category": {
            "id": 1,
            "name": "Report"
        },
        "author": {
            "id": 2,
            "username": "alice"
        },
        "can_create": false,
        "can_read": true,
        "can_update": false,
        "can_delete": false
    }
]
```
