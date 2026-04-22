from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ping_route import router as ping_router
from app.routes.todo_route import router as todo_router
from app.settings import settings

app = FastAPI(title=settings.project_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ping_router)
app.include_router(todo_router)
