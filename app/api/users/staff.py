from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.oauth_scheme import Token
from app.schemas.user_scheme import StaffAuthModel, StaffViewModel

from app.api.actions.auth import authenticate_staff, get_current_staff
from app.api.dependencies import staff_service
from app.services.user_service import StaffService
from app.models.development import Staff
from app.security import create_access_token_for_staff
from app.api.actions.permissions import isAdmin


router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: StaffAuthModel) -> Token:
    staff = await authenticate_staff(id=form_data.id, password=form_data.password)

    if not staff:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect id or password",
        )

    access_token = create_access_token_for_staff(data={"id": staff.id})
    return Token(access_token=access_token)


@router.get("/users", response_model=List[StaffViewModel])
@isAdmin
async def profile(
    current_staff: Annotated[Staff, Depends(get_current_staff)],
    staff_service: Annotated[StaffService, Depends(staff_service)],
) -> List[StaffViewModel]:

    return await staff_service.get_all()
