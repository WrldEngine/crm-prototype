from datetime import timedelta
from sqlalchemy import delete, func

from app.models.development import Tasks
from app.core.database import async_session


class TasksService:
    @staticmethod
    async def delete_exp():
        async with async_session() as session:
            query = delete(Tasks).where(Tasks.deadline < func.now())

            await session.execute(query)
            await session.commit()
