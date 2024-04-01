from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.exc import IntegrityError

from app.api.actions.auth import authenticate_client, get_current_client
from app.api.actions.verification import verify_email, create_verification_token
from app.api.dependencies import clients_service
from app.security import create_access_token

from app.schemas.user_scheme import (
    ClientCreationModel,
    ClientViewModel,
    ClientAuthModel,
)
from app.schemas.oauth_scheme import Token
from app.services.user_service import ClientsService
from app.models.users import Client

from celery_tasks.tasks import email_send_verification_link


router = APIRouter()


@router.post("/reg", response_model=ClientViewModel)
async def create_client(
    client: ClientCreationModel,
    request: Request,
    clients_service: Annotated[ClientsService, Depends(clients_service)],
) -> ClientViewModel:
    try:
        client = await clients_service.create(client)

    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="This username or email already exists",
        )

    _verification_token = create_verification_token({"email": client.email})
    _verification_link = f"{request.base_url}clients/verify/{_verification_token}"

    email_send_verification_link.delay(
        client.username,
        _verification_link,
        client.email,
    )

    return client


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: ClientAuthModel) -> Token:
    client = await authenticate_client(
        username=form_data.username, password=form_data.password
    )

    if not client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(data={"sub": client.username})
    return Token(access_token=access_token)


@router.get("/{username}/profile", response_model=ClientViewModel)
async def get_profile(
    username: str,
    current_client: Annotated[Client, Depends(get_current_client)],
    clients_service: Annotated[ClientsService, Depends(clients_service)],
) -> ClientViewModel:

    return await clients_service.get_single(username=username)


@router.get("/verify/{token}")
async def verify_client(token: str) -> Any:
    verify_client = await verify_email(token)

    if not verify_client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return status.HTTP_200_OK
