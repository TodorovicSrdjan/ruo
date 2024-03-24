import uvicorn

from fastapi import FastAPI
from routers import todo_router

app = FastAPI()
app.include_router(todo_router.router, prefix="/api/v1/todos")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", log_level="info")