# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
#
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
#
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.

from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str


tasks = []
task1 = Task(id=1, title="Квадрат суммы", description="очень крутая задача", status="не выполнена")
task2 = Task(id=1, title="Разность квадратов", description="известная задача", status="выполняется")
tasks.append(task1)
tasks.append(task2)


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.post("/tasks", status_code=201)
async def create_task(task: Task):
    tasks.append(task)
    return "Задача добавлена"


@app.put("/tasks/{task_id}", status_code=200)
async def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return "Задача обновлена"
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/tasks/{task_id}", status_code=200)
async def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return "Задача удалена"
