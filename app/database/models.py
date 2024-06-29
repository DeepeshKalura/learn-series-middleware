import datetime
import pytz
from sqlalchemy import Integer, String, Column, DateTime

from .db import Base 


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String, unique=True)
    password = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(pytz.UTC))




