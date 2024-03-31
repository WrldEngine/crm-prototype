from app.models.development import Tasks
from app.repositories.tasks_repository import TasksRepository
from app.schemas.tasks_scheme import TaskCreationModel


class TasksService:
    def __init__(self, tasks_repo: TasksRepository):
        self.tasks_repo: TasksRepository = tasks_repo(model=Tasks)

    async def create(self, task: TaskCreationModel) -> TaskCreationModel:
        task_dict = task.model_dump()
        return await self.tasks_repo.create(task_dict)

    async def get_single(self, **filters):
        return await self.tasks_repo.get_single(**filters)

    async def update(self, data: dict, **filters):
        task_dict = data.model_dump()
        return await self.tasks_repo.update(task_dict, **filters)

    async def add_member(self, task_id, staff_id):
        return await self.tasks_repo.add_member(task_id, staff_id)

    async def delete(self, **filters):
        await self.tasks_repo.delete(**filters)

    async def get_all(self):
        return await self.tasks_repo.get_all()
