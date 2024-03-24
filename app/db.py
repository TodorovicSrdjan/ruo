import imp
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# DATABASE_URL = os.getenv("DATABASE_URL")  # TODO
DB_USER = os.getenv("DB_USER")
DB_PW = os.getenv("DB_PW")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PW}@db:{DB_PORT}/{DB_NAME}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 