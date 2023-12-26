import uvicorn

if __name__ == '__main__':
    app = 'seminars.sem_5.pack_4.task_4:app'
    uvicorn.run(app, port=8000, reload=True)
