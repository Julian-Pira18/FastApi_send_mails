from src.config.database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean


class Course(Base):

    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    photo_url = Column(String)
    is_public = Column(Boolean)
    rquirements = Column(String)
    max_amount_students = Column(Integer)
    author_id = Column(Integer)
    professor_id = Column(Integer)
    created_at = Column(String)

# Base.metadata.create_all(bind=engine)
