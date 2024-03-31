import pytest
from .app_test import cli


@pytest.mark.asyncio
def test_login(cli):
    response = cli.post(
        "/clients/login", json={"username": "callistodev1", "password": "12345"}
    )

    assert response.status_code == 401


@pytest.mark.asyncio
def test_validation(cli):
    response = cli.post(
        "/clients/reg",
        json={
            "first_name": "10j4hd",
            "last_name": "2h3h3h",
            "username": "herllo",
            "password": "11",
            "gender": "uzbek",
            "email": "some_incorrect-test",
        },
    )

    assert response.status_code == 422


@pytest.mark.asyncio
def test_get_client_profile(cli):
    response = cli.get("/clients/string/profile")

    assert response.status_code == 401
    assert response.json() == {"detail": "Could not Validate Credentials"}
