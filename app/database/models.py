import datetime
from sqlalchemy import Integer, String, Column, DateTime

from .database import Base 


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String, unique=True)
    password = Column(String)
    create_at = Column(DateTime, default=datetime.UTC)




