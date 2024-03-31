from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import tasks_service
from app.api.actions.auth import get_current_staff
from app.services.task_service import TasksService
from app.models.development import Staff, Tasks
from app.schemas.tasks_scheme import TaskCreationModel, TaskUpdateModel, TaskShowModel
from app.api.actions.permissions import isAdmin, isAdminOrCurator

router = APIRouter()


@router.post("/create_task", response_model=TaskCreationModel)
@isAdmin
async def create_task(
    task_model: TaskCreationModel,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
) -> TaskCreationModel:

    return await tasks_service.create(task_model)


@router.get("/all", response_model=List[TaskShowModel])
async def create_task(
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
) -> TaskShowModel:

    return await tasks_service.get_all()


@router.put("/{task_id}/edit", response_model=TaskUpdateModel)
@isAdminOrCurator
async def edit_task(
    task_id: int,
    task_model: TaskUpdateModel,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
) -> TaskUpdateModel:

    return await tasks_service.update(task_model, id=task_id)


@router.put("/{task_id}/add_member/{staff_id}", response_model=TaskShowModel)
@isAdminOrCurator
async def edit_task(
    task_id: int,
    staff_id: int,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
) -> TaskShowModel:

    return await tasks_service.add_member(task_id, staff_id)


@router.delete("/{task_id}/delete")
@isAdmin
async def delete_task(
    task_id: int,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
) -> Any:
    await tasks_service.delete(id=task_id)

    return status.HTTP_200_OK
