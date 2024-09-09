from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.assocaitions import user_course
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Course(Base):

    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    photo_url = Column(String)
    is_public = Column(Boolean)
    rquirements = Column(String)
    max_amount_students = Column(Integer)

    author_id = Column(Integer, ForeignKey('users.id'))

    professor_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, server_default=func.now())

    author = relationship("User", foreign_keys=[
        author_id], back_populates="authored_courses")
    professor = relationship("User", foreign_keys=[
        professor_id], back_populates="taught_courses")
    events = relationship("Event", back_populates="course")
    users = relationship("User", secondary=user_course,
                         back_populates="courses")


Base.metadata.create_all(bind=engine)
