import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from .database import Session as SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


Session = sessionmaker(bind=engine)

Base = declarative_base()
