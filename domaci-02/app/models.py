from sqlalchemy import Column, Integer, String
from db import Base

class Todo(Base):
    __tablename__ = "todos"

    id          = Column(Integer, primary_key=True)
    title       = Column(String(40))
    description = Column(String(200))