import uvicorn

if __name__ == "__main__":
    uvicorn.run("lecture.lect_6.models_3:app", port=80, reload=True)
