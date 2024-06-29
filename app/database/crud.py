from typing import Optional
from sqlalchemy.orm import Session

from app.schema.user_schema import UserBaseModel

from app.database.models import User 



def get_user(db:Session, user_id:Optional[int]):
    if(user_id != None):
        return db.query(User).filter(User.id  == user_id).first()

    else:
        return db.query(User).all()
    

def create_user(db: Session, user:UserBaseModel):
    
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
