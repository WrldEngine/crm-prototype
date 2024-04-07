import pytest

from .conftest import async_client
from httpx import AsyncClient


class TestAdminAndStaff:

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "id, password, status",
        [
            ("1", "hello_world", 200),
            ("2", "noadmin", 401),
        ]
    )
    async def test_admin_login(self, id, password, status, async_client: AsyncClient):
        response = await async_client.post(
            "/staff/login",
            json={
                "id": id,
                "password": password,
            },
        )

        assert response.status_code == status
        return response.json()["access_token"] if response.status_code == 200 else None

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "first_name, last_name, patronymic, email, phone_number, assigned_position, gender, password, status",
        [
            (
                "teststaff",
                "teststaff",
                "teststaff",
                "hello@gmail.com",
                "1222111",
                "BACKEND",
                "MALE",
                "1234567",
                200,
            ),
            (
                "test_staff2",
                "test_staff2",
                "test_staff2",
                "userexample.com",
                "1222",
                "DESIGNs",
                "FEMALEs",
                "12345",
                422,
            ),
        ],
    )
    async def test_create_staff(
        self,
        first_name,
        last_name,
        patronymic,
        email,
        phone_number,
        assigned_position,
        gender,
        password,
        status,
        async_client: AsyncClient,
    ):
        token = await self.test_admin_login("1", "hello_world", 200, async_client)

        response = await async_client.post(
            f"/admin/create_staff?token={token}",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "patronymic": patronymic,
                "email": email,
                "phone_number": phone_number,
                "assigned_position": assigned_position,
                "gender": gender,
                "password": password,
            },
        )

        assert response.status_code == status
    
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "title, description, position, status",
        [
            ("test_task_title", "test_task_desc", "DESIGN", 200),
            ("test_task_title", "test_task_desc", "NODESIGN", 422),
        ]
    )
    async def test_create_task(self, title, description, position, status, async_client: AsyncClient):
        token = await self.test_admin_login("1", "hello_world", 200, async_client)

        response = await async_client.post(
            f"/tasks/create_task?token={token}",
            json={
                "title": title,
                "description": description,
                "position": position,
                "curator_id": 1,
            },
        )

        assert response.status_code == status

    @pytest.mark.asyncio
    async def test_view_tasks(self, async_client: AsyncClient):
        response = await async_client.get("/tasks/all")

        assert response.status_code == 200
        assert response.json() is not None