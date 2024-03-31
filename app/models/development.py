from typing import List
from datetime import datetime, timedelta

from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, Column, ForeignKey, func

from app.models.enums import Positions, GenderStatus

association_table = Table(
    "association_table",
    Base.metadata,
    Column("tasks_id", ForeignKey("tasks.id")),
    Column("staff_id", ForeignKey("staff.id")),
)


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40))
    description: Mapped[str]

    deadline: Mapped[datetime] = mapped_column(
        default=(func.now() + timedelta(days=30))
    )
    position: Mapped[Positions]

    curator_id: Mapped[int] = mapped_column(ForeignKey("staff.id", ondelete="CASCADE"))
    participants: Mapped[List["Staff"]] = relationship(
        secondary=association_table, lazy="selectin"
    )


class Staff(Base):
    __tablename__ = "staff"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    patronymic: Mapped[str] = mapped_column(String(40))

    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str]

    gender: Mapped[GenderStatus]
    password: Mapped[str]

    assigned_position: Mapped[Positions]
    owned_tasks: Mapped[List["Tasks"]] = relationship("Tasks", lazy="subquery")
    participation: Mapped[List["Tasks"]] = relationship(secondary=association_table)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
