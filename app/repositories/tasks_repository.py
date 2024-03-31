from typing import TypeVar, Optional
from sqlalchemy import delete, select, update
from app.core.database import async_session
from app.models.development import Staff

from .base_repository import AbstractRepository


class TasksRepository(AbstractRepository):
    def __init__(self, model):
        self.model = model

    async def create(self, data: dict):
        async with async_session() as session:
            instance = self.model(**data)

            session.add(instance)
            await session.commit()
            await session.refresh(instance)

            return instance

    async def update(self, data: dict, **filters) -> TypeVar:
        async with async_session() as session:
            query = (
                update(self.model)
                .values(**data)
                .filter_by(**filters)
                .returning(self.model)
            )

            result = await session.execute(query)
            await session.commit()

            return result.scalar_one()

    async def add_member(self, task_id, staff_id) -> TypeVar:
        async with async_session() as session:
            task = await session.execute(select(self.model).filter_by(id=task_id))
            staff = await session.execute(select(Staff).filter_by(id=staff_id))

            task_row = task.scalars().unique().one()
            staff_row = staff.scalars().unique().one()

            task_row.participants.append(staff_row)

            await session.commit()
            return task_row

    async def delete(self, **filters) -> None:
        async with async_session() as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> Optional[TypeVar] | None:
        async with async_session() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def get_all(
        self, order: str = "id", limit: int = 100, offset: int = 0
    ) -> list[TypeVar]:
        async with async_session() as session:
            query = select(self.model)

            row = await session.execute(query)
            return row.scalars().all()
