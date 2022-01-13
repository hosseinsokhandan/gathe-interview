import asyncio
from pytest import fixture
from tortoise import Tortoise
from models.member import Member
from models.document import Category, Document
from settings import get_settings


settings = get_settings()
DB_URL = "sqlite://:memory:"


async def init_db() -> None:
    """Initial database connection"""
    await Tortoise.init(
        db_url=DB_URL, modules={"models": settings.MODELS}, _create_db=True
    )
    await Tortoise.generate_schemas()


@fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@fixture(scope="function", autouse=True)
async def initialize_test():
    await init_db()
    yield
    await Tortoise._drop_databases()


@fixture(scope="function")
async def provide_test_data() -> None:
    await Member.create(id=1, username="admin")
    await Member.create(id=2, username="user2")
    await Member.create(id=3, username="user3")

    await Category.create(id=1, name="Category 1")
    await Category.create(id=2, name="Category 2")
    await Category.create(id=3, name="Category 3")

    await Document.create(
        id=1, subject="Subject 1", content="Content 1", author_id=1, category_id=1
    )
    await Document.create(
        id=2, subject="Subject 2", content="Content 2", author_id=2, category_id=2
    )
    await Document.create(
        id=3, subject="Subject 3", content="Content 3", author_id=3, category_id=2
    )
    await Document.create(
        id=4, subject="Subject 4", content="Content 3", author_id=3, category_id=2
    )


@fixture
async def admin_header():
    return {"username": "admin"}


@fixture
async def non_admin_header():
    return {"username": "user2"}
