"""Форматирование ответов API"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def read_root():
    """HTML текст"""
    return '<H1>Hello World</H1>'


@app.get('/message/')
async def read_message():
    """JSON объект"""
    message = {'message': "Hello Worls"}
    return JSONResponse(content=message, status_code=200)


# допустыми использование обоих вариантов  и с HTMLResponse и с JsonResponse