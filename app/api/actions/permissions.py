from functools import wraps
from fastapi import HTTPException, status


def isAdmin(func):
    @wraps(func)
    async def has_permission(**kwargs):
        current_staff = kwargs["current_staff"]

        if not current_staff.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource.",
            )

        return await func(**kwargs)

    return has_permission


def isAdminOrCurator(func):
    @wraps(func)
    async def has_permission(**kwargs):
        task_id = kwargs["task_id"]
        current_staff = kwargs["current_staff"]

        owned_tasks = [task.id for task in current_staff.owned_tasks]

        if (not current_staff.is_superuser) and (task_id not in owned_tasks):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource.",
            )

        return await func(**kwargs)

    return has_permission
