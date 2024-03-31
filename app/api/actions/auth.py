from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, ExpiredSignatureError, jwt

from app.core.project_config import settings
from app.utils import verify_password
from app.api.dependencies import clients_service, staff_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/clients/login")


async def get_current_client(
    token: str = Annotated[str, Depends(oauth2_scheme)],
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials",
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    client = await clients_service().get_single(username=username)
    if not client:
        raise credentials_exception

    return client


async def get_current_staff(token: str = Annotated[str, Depends(oauth2_scheme)]):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials",
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY_STAFF, algorithms=[settings.ALGORITHM]
        )
        id = payload.get("id")

        if id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    staff = await staff_service().get_single(id=id)
    if not staff:
        raise credentials_exception

    return staff


async def authenticate_client(username: str, password: str):
    client = await clients_service().get_single(username=username)

    if not client:
        return False

    if not verify_password(password, client.password):
        return False

    return client


async def authenticate_staff(id: int, password: str):
    staff = await staff_service().get_single(id=id)

    if not staff:
        return False

    if not verify_password(password, staff.password):
        return False

    return staff
