from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.models import Todo, TodoCreate, TodoPatch, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

todos: dict[int, Todo] = {}
next_id = 1


@router.get("", response_model=list[Todo], operation_id="get_todos")
def get_todos():
    return list(todos.values())


@router.post("", response_model=Todo, status_code=201, operation_id="create_todo")
def create_todo(body: TodoCreate):
    global next_id
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
def get_todo(todo_id: int):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=Todo, operation_id="update_todo")
def update_todo(todo_id: int, body: TodoUpdate):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated = todo.model_copy(update={"title": body.title, "completed": body.completed})
    todos[todo_id] = updated
    return updated


@router.patch("/{todo_id}", response_model=Todo, operation_id="patch_todo")
def patch_todo(todo_id: int, body: TodoPatch):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    patch_data = body.model_dump(exclude_unset=True)
    updated = todo.model_copy(update=patch_data)
    todos[todo_id] = updated
    return updated


@router.delete("/{todo_id}", status_code=204, operation_id="delete_todo")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
