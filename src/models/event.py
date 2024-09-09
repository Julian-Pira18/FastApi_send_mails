from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Event(Base):

    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime, server_default=func.now())
    course_id = Column(Integer, ForeignKey(
        'course.id'))
    event_link = Column(String)

    course = relationship("Course", back_populates="events")


Base.metadata.create_all(bind=engine)
