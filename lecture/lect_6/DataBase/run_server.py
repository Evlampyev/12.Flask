import uvicorn

if __name__ == "__main__":
    uvicorn.run("lecture.lect_6.DataBase.task_1:app", port=80, reload=True)
