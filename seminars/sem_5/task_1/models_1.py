# Создайте класс Task с полями id, title, description и status.

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: bool = False
