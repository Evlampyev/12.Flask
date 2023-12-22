from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    description: str | None = None
    genre: str
