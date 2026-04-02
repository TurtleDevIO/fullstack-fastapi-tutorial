# src/backend/main.py
from fastapi import FastAPI

from settings import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": f"Hello World! Welcome to {settings.project_name} and {settings.test}"}
