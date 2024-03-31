from app.services.user_service import ClientsService, StaffService
from app.repositories.users_repository import UsersRepository

from app.services.task_service import TasksService
from app.repositories.tasks_repository import TasksRepository


def clients_service():
    return ClientsService(UsersRepository)


def staff_service():
    return StaffService(UsersRepository)


def tasks_service():
    return TasksService(TasksRepository)
