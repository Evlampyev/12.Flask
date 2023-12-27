from pydantic import BaseModel


class Task(BaseModel):
    task_id: int
    title: str
    locality: str | None = None
    status: bool = False
