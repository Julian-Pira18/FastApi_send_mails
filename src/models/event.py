from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean


class Event(Base):

    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    course_id = Column(Integer)
    event_link = Column(String)


# Base.metadata.create_all(bind=engine)
