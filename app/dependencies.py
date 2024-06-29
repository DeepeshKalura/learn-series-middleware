# dababase dependencies
from app.database import db


def get_db():
    deb = db.local_session()
    try:
        yield deb 
    finally:
        deb.close()