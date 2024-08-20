from typing import AsyncGenerator, Generator
from app import app
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
import pytest_asyncio
from faker import Faker
from app.service.admin_service import AdminService
from app.service.geolocator.geolocator import Geolocator


@pytest_asyncio.fixture(scope="session")
def anyio_backend():
    return "asyncio"



@pytest_asyncio.fixture(scope="session")
def client() -> Generator:
    yield TestClient(app)



@pytest_asyncio.fixture(scope="session", autouse=True)
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=client.base_url) as ac:
        yield ac



@pytest_asyncio.fixture(scope="session")
def fake():
    return Faker(locale="ru")



@pytest_asyncio.fixture(scope="session")
def admin_key():
    return AdminService().new_key()



@pytest_asyncio.fixture(scope="session")
def coordinate():
    return Geolocator()