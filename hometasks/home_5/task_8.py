from fastapi import FastAPI, Request, Form
from hometasks.home_5.models import Task
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')
tasks: list[Task] = []


@app.get('/')
@app.get('/tasks/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        'users.html', {'request': request, 'tasks': tasks})


@app.get('/tasks/{task_id}')
def get__id_task(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            return task
    else:
        return f'Нет задачи с таким id'


@app.post('/tasks/')
def add_task(request: Request,
             title: str = Form(...),
             locality: str = Form(...),
             status: str = Form(...),
             task_id: int = Form(...),
             ):
    task = Task(
        task_id=task_id,
        title=title,
        locality=locality,
        status=status,
    )
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
def change_task(task_id: int, new_task: Task):
    filtered_task = [task for task in tasks if task.task_id == task_id]
    if not filtered_task:
        return {'updated': False}
    task = filtered_task[0]
    # print(f'{new_task = }, {new_task.title = }')
    if new_task.title != "string":
        task.title = new_task.title
    if new_task.l != "string":
        task.locality = new_task.locality
    task.status = new_task.status
    return {'updated': True, 'task': task}


@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.task_id == task_id]
    if not filtered_tasks:
        return {'deleted': False}

    tasks.remove(filtered_tasks[0])
    return {'deleted': True, 'task': filtered_tasks[0]}
