FROM python:3.10-slim

COPY . /app 

RUN pip install 'fastapi[all]' && pip install uvicorn

EXPOSE 5000

CMD ["python", "/app/app.py"]