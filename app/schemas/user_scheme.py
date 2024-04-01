import re

from .base_scheme import Base
from app.models.enums import GenderStatus, Positions

from pydantic import validator, EmailStr

from fastapi import HTTPException, status

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")
USERNAME_LETTER_MATCH_PATTERN = re.compile(r"^[a-zA-Z]")
MAX_PASSWORD_LENGTH = 3


class ClientCreationModel(Base):
    username: str
    first_name: str
    last_name: str
    password: str
    gender: GenderStatus
    email: EmailStr

    @validator("username")
    def validate_username(cls, value):
        if not USERNAME_LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Username should contain only letters",
            )
        return value

    @validator("first_name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Name should contain only letters",
            )
        return value

    @validator("last_name")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Surname should contain only letters",
            )
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < MAX_PASSWORD_LENGTH:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Password can not contain less than {MAX_PASSWORD_LENGTH} symbols",
            )
        return value


class ClientAuthModel(Base):
    username: str
    password: str


class ClientViewModel(Base):
    id: int
    username: str
    first_name: str
    last_name: str
    gender: str
    is_verified: bool


class StaffAuthModel(Base):
    id: int
    password: str


class StaffViewModel(Base):
    id: int
    first_name: str
    last_name: str
    patronymic: str
    phone_number: str
    assigned_position: Positions


class StaffCreationModel(Base):
    first_name: str
    last_name: str
    patronymic: str
    email: EmailStr
    phone_number: str
    assigned_position: Positions
    gender: GenderStatus
    password: str

    @validator("first_name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Name should contain only letters",
            )
        return value

    @validator("last_name")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Surname should contain only letters",
            )
        return value

    @validator("patronymic")
    def validate_patronymic(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Patronymic should contain only letters",
            )
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < MAX_PASSWORD_LENGTH:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Password can not contain less than {MAX_PASSWORD_LENGTH} symbols",
            )
        return value
