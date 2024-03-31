import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="module")
def cli():
    yield TestClient(app)
