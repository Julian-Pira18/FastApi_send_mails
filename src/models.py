from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

user_course = Table('user_course', Base.metadata,
                    Column('user_id', Integer, ForeignKey(
                        'users.id'), primary_key=True),
                    Column('course_id', Integer, ForeignKey(
                        'course.id'), primary_key=True)
                    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    photo_url = Column(String)
    role_id = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    # Relaciones
    authored_courses = relationship(
        "Course", foreign_keys='Course.author_id', back_populates="author")
    taught_courses = relationship(
        "Course", foreign_keys='Course.professor_id', back_populates="professor")
    courses = relationship(
        "Course", secondary=user_course, back_populates="users")


class Event(Base):

    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime, server_default=func.now())
    course_id = Column(Integer, ForeignKey(
        'course.id'))
    event_link = Column(String)

    course = relationship("Course", back_populates="events")


# Tabla intermedia para la relación muchos a muchos entre 'User' y 'Course'


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
