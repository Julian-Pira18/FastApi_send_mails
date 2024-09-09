from sqlalchemy import Table, Column, Integer, ForeignKey
from src.config.database import Base, engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Tabla intermedia para la relación muchos a muchos entre 'User' y 'Course'
user_course = Table('user_course', Base.metadata,
                    Column('user_id', Integer, ForeignKey(
                        'users.id'), primary_key=True),
                    Column('course_id', Integer, ForeignKey(
                        'course.id'), primary_key=True)
                    )

Base.metadata.create_all(bind=engine)
