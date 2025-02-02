from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

DB_URL = "sqlite:///database.db"
engine = create_engine(
    DB_URL, connect_args= {"check_same_thread": False}
)

local_session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

