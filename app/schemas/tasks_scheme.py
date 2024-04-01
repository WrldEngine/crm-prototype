from typing import Optional, List
from .base_scheme import Base
from app.models.enums import Positions

from datetime import datetime


class TaskCreationModel(Base):
    title: str
    description: str
    position: Positions
    curator_id: int


class Member(Base):
    id: int
    first_name: str


class TaskShowModel(Base):
    title: str
    description: str
    position: Positions
    deadline: datetime
    participants: List[Member]


class TaskUpdateModel(Base):
    title: str
    description: str
