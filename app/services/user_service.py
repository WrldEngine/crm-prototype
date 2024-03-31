from app.schemas.user_scheme import ClientCreationModel, StaffCreationModel
from app.repositories.users_repository import UsersRepository

from app.models.users import Client
from app.models.development import Staff


class ClientsService:
    def __init__(self, clients_repo: UsersRepository):
        self.clients_repo: UsersRepository = clients_repo(model=Client)

    async def create(self, client: ClientCreationModel) -> ClientCreationModel:
        client_dict = client.model_dump()
        client = await self.clients_repo.create(client_dict)

        return client

    async def update(self, data: dict, **filters):
        client_dict = data.model_dump()
        updated_client = await self.clients_repo.update(client_dict, **filters)

        return updated_client

    async def get_single(self, **filters):
        client = await self.clients_repo.get_single(**filters)
        return client

    async def get_all(self):
        get_all_users = await self.clients_repo.get_all()
        return get_all_users


class StaffService:
    def __init__(self, staff_repo: UsersRepository):
        self.staff_repo: UsersRepository = staff_repo(model=Staff)

    async def create(self, staff: StaffCreationModel) -> StaffCreationModel:
        staff_dict = staff.model_dump()
        staff = await self.staff_repo.create(staff_dict)

        return staff

    async def update(self, data: dict, **filters):
        staff_dict = data.model_dump()
        updated_staff = await self.staff_repo.update(staff_dict, **filters)

        return updated_staff

    async def get_single(self, **filters):
        staff = await self.staff_repo.get_single(**filters)
        return staff

    async def delete(self, **filters):
        await self.staff_repo.delete(**filters)

    async def get_all(self):
        get_all_users = await self.staff_repo.get_all()
        return get_all_users
