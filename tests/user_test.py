import pytest

from .conftest import async_client
from httpx import AsyncClient


class TestClientAuth:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "username, first_name, last_name, password, gender, email, status",
        [
            (
                "test_client",
                "string",
                "string",
                "string",
                "MALE",
                "kamscienceit123.kamran@gmail.com",
                200,
            ),
            ("test_cli", "sss", "sss", "ss", "NOGENDER", "noemail", 422),
        ],
    )
    async def test_validation(
        self,
        username,
        first_name,
        last_name,
        password,
        gender,
        email,
        status,
        async_client: AsyncClient,
    ):
        response = await async_client.post(
            "/clients/reg",
            json={
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
                "gender": gender,
                "email": email,
            },
        )

        assert response.status_code == status

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "username, password, status",
        [
            ("this_account_does_not_exist", "some_incorrect_password", 401),
            ("lazyboy", "ffsssdd", 401),
            ("maxin", "fjjsdsd", 401),
            ("maxin", "string", 401),
            ("string", "string", 401),
            ("test_client", "string", 200),
        ],
    )
    async def test_login(self, username, password, status, async_client: AsyncClient):
        response = await async_client.post(
            "/clients/login", json={"username": username, "password": password}
        )

        assert response.status_code == status
        return response.json()["access_token"] if response.status_code == 200 else None

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "username, password, status",
        [
            ("test_client", "string", 200),
            ("notest_cli", "sfff", 401),
        ],
    )
    async def test_get_client_profile(
        self, username, password, status, async_client: AsyncClient
    ):
        token = await self.test_login(username, password, status, async_client)

        response = await async_client.get(
            f"/clients/{username}/profile",
            params={
                "token": token,
            },
        )

        assert response.status_code == status
