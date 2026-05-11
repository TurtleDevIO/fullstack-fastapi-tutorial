import asyncio
import random
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.models import Todo, TodoCreate, TodoPatch, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

todos: dict[int, Todo] = {}
next_id = 1

# Artificial delay and random errors to make loading/error states visible in the tutorial.
# Remove these in a real application.
SIMULATED_DELAY = 1.0
ERROR_RATE = 0.2


def maybe_fail():
    if random.random() < ERROR_RATE:
        raise HTTPException(status_code=500, detail="Simulated server error")


@router.get("", response_model=list[Todo], operation_id="get_todos")
async def get_todos():
    await asyncio.sleep(SIMULATED_DELAY)
    return list(todos.values())


@router.post("", response_model=Todo, status_code=201, operation_id="create_todo")
async def create_todo(body: TodoCreate):
    global next_id
    await asyncio.sleep(SIMULATED_DELAY)
    maybe_fail()
    todo = Todo(
        id=next_id,
        title=body.title,
        completed=False,
        created_at=datetime.now(timezone.utc),
    )
    todos[next_id] = todo
    next_id += 1
    return todo


@router.get("/{todo_id}", response_model=Todo, operation_id="get_todo")
async def get_todo(todo_id: int):
    await asyncio.sleep(SIMULATED_DELAY)
    maybe_fail()
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=Todo, operation_id="update_todo")
async def update_todo(todo_id: int, body: TodoUpdate):
    await asyncio.sleep(SIMULATED_DELAY)
    maybe_fail()
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated = todo.model_copy(update={"title": body.title, "completed": body.completed})
    todos[todo_id] = updated
    return updated


@router.patch("/{todo_id}", response_model=Todo, operation_id="patch_todo")
async def patch_todo(todo_id: int, body: TodoPatch):
    await asyncio.sleep(SIMULATED_DELAY)
    maybe_fail()
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    patch_data = body.model_dump(exclude_unset=True)
    updated = todo.model_copy(update=patch_data)
    todos[todo_id] = updated
    return updated


@router.delete("/{todo_id}", status_code=204, operation_id="delete_todo")
async def delete_todo(todo_id: int):
    await asyncio.sleep(SIMULATED_DELAY)
    maybe_fail()
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
