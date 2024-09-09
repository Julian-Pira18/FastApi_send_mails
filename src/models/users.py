from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.assocaitions import user_course  # Importar la tabla intermedia
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


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


Base.metadata.create_all(bind=engine)
