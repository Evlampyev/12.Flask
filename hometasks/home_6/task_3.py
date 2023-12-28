# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.


from contextlib import asynccontextmanager
# Вместо двух функций, создаём asynccontextmanager
from fastapi import FastAPI, Request, Form
from hometasks.home_6.pydantic_models import Task
from hometasks.home_6.sqlalchemy_models import Base, Task as SqlTask
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, select, insert, update, delete
from databases import Database

DATABASE_URL = "sqlite:///task_3_db.db"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()

    yield

    await database.disconnect()


app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory='templates')


@app.get('/')
@app.get('/tasks/', response_class=HTMLResponse)
async def index(request: Request):
    query = select(SqlTask)
    tasks = await database.fetch_all(query)
    return templates.TemplateResponse(
        'users.html', {'request': request, 'tasks': tasks})


@app.get('/tasks/{task_id}')
def get__id_task(task_id: int):
    query = select(SqlTask).where(SqlTask.task_id == task_id)
    task = database.fetch_one(query)
    if not task:
        return f'Нет задачи с таким id'
    else:
        return task


@app.post('/tasks/')
async def add_task(request: Request,
                   title: str = Form(...),
                   locality: str = Form(...),
                   status: bool = Form(False),
                   ):
    new_task = insert(SqlTask).values(title=title, locality=locality,
                                      status=status)
    await database.execute(new_task)
    tasks = await database.fetch_all(select(SqlTask))
    return templates.TemplateResponse(
        'users.html', {'request': request, 'tasks': tasks})


@app.put('/tasks/{task_id}')
async def change_task(task_id: int, new_task: Task):
    query = select(SqlTask).where(SqlTask.task_id == task_id)
    task = await database.fetch_one(query)
    if not task:
        return {'updated': False}
    # print(f'{new_task = }, {new_task.title = }')
    query = (
        update(SqlTask)
        .where(SqlTask.task_id == task_id)
        .values(**new_task.model_dump())
    )
    await database.execute(query)
    return {'updated': True, 'task': task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    query = select(SqlTask).where(SqlTask.task_id == task_id)
    filtered_tasks = await database.fetch_one(query)
    if not filtered_tasks:
        return {'deleted': False}

    deleted_task = delete(SqlTask).where(SqlTask.task_id == task_id)
    await database.execute(deleted_task)
    return {'deleted': True, 'deleted_task': task_id}
