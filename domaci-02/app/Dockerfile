FROM python:3.10-slim

COPY . /app 

RUN pip install --no-cache-dir 'fastapi[all]' uvicorn SQLAlchemy psycopg2-binary

EXPOSE 8000

ENTRYPOINT ["python", "/app/app.py"]