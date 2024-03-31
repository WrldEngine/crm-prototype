from fastapi import APIRouter

from .users.client import router as client_router
from .users.staff import router as staff_router
from .users.admin import router as admin_router
from .management.tasks import router as tasks_router

v1 = APIRouter()

v1.include_router(client_router, prefix="/clients", tags=["clients"])
v1.include_router(staff_router, prefix="/staff", tags=["staff"])
v1.include_router(admin_router, prefix="/admin", tags=["admin"])
v1.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
