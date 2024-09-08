from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(bind=engine)
