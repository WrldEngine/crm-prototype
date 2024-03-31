from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from celery_tasks.tasks import admin_send_email

from app.schemas.user_scheme import StaffCreationModel, StaffViewModel
from app.schemas.admin_scheme import SendEmail
from app.api.actions.auth import get_current_staff
from app.api.dependencies import staff_service
from app.services.user_service import StaffService
from app.models.development import Staff
from app.api.actions.permissions import isAdmin


router = APIRouter()


@router.post("/send_email")
@isAdmin
async def send_email(
    format_message: SendEmail,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
) -> Any:

    admin_send_email.delay(
        subject=format_message.subject,
        main_content=format_message.main_content,
        to_emails=format_message.email_list,
    )

    return status.HTTP_200_OK


@router.post("/create_staff", response_model=StaffViewModel)
@isAdmin
async def create_staff(
    staff_model: StaffCreationModel,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    staff_service: Annotated[StaffService, Depends(staff_service)],
) -> StaffViewModel:

    return await staff_service.create(staff_model)


@router.delete("/delete_staff/{staff_id}")
@isAdmin
async def delete_staff(
    staff_id: int,
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    staff_service: Annotated[StaffService, Depends(staff_service)],
) -> Any:
    await staff_service.delete(id=staff_id)
    return status.HTTP_200_OK
