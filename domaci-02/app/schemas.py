from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: str


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    title: str
    description: str