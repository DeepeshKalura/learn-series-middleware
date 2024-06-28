from typing import Optional
from sqlalchemy.orm import Session

from app.schema.user_schema import UserBaseModel

from . import models 



def get_user(db:Session, user_id:Optional[int]):
    if(type(user_id) == int):
        return db.query(models.User).filter(models.User.id  == user_id).first()

    else:
        return db.query(models)
    

def create_user(db: Session, user:UserBaseModel):
    
    db_user = models.User(user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
