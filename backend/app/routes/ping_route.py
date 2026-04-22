from fastapi import APIRouter

from app.settings import settings

router = APIRouter(tags=["ping"])


@router.get("/ping", operation_id="ping")
def ping():
    return {"message": f"Hello World! Welcome to {settings.project_name}."}
