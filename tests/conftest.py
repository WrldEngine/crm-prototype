import pytest
import asyncio

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine

from main import app

from app.models.base_model import Base
from app.core.project_config import settings
from app.create_superuser import admin_auto_creation

DATABASE_URL = settings.build_postgres_dsn()

engine_test = create_async_engine(DATABASE_URL, echo=settings.DB_ECHO)


@pytest.fixture(autouse=True, scope="session")
async def prepare_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(autouse=True)
async def admin_create():
    await admin_auto_creation()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as cli:
        yield cli
