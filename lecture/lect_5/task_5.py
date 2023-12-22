"""Динамический HTML через шаблонизатор Jinja"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#  Jinja2Templates - шаблонизатор
app = FastAPI()
templates = Jinja2Templates(directory="./lecture/lect_5/templates")


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    # request обязательный аргумент
    return templates.TemplateResponse("item.html", {"request": request, "name": name})


@app.get('/')
async def read_root():
    return {'Hello': "world"}
