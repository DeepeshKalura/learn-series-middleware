from fastapi import APIRouter, Depends, Request
import pytz
from app.schema.user_schema import UserBaseModel 
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.database import crud 

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# middle ware
@router.get("/")
async def list_of_user(db:Session= Depends(get_db)):
    return crud.get_user(db=db, user_id=None)


@router.get("/{id}")
async def list_user(request:Request, id=id, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=id)
    print(user.create_at)

    cts = user.create_at
    user.create_at = cts.astimezone(pytz.timezone(request.headers.get("x-timezone")))

    return user
    

@router.post("/")
async def get_create_user(user:UserBaseModel, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user) 
        