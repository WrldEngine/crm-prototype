from typing import Optional, List
from .base_scheme import Base, OrmSchemeModel
from app.models.enums import Positions
from app.models.development import Staff

from datetime import datetime


class TaskCreationModel(OrmSchemeModel):
    title: str
    description: str
    position: Positions
    curator_id: int


class TaskShowModel(OrmSchemeModel):
    title: str
    description: str
    position: Positions
    deadline: datetime


class TaskUpdateModel(OrmSchemeModel):
    title: str
    description: str
