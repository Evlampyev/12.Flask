from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Boolean

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    title = Column(String(50))
    locality = Column(String(50))
    status = Column(Boolean)
