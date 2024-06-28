from fastapi import APIRouter, Depends
from main import get_db
from schema.user_schema import UserBaseModel 
from sqlalchemy.orm import Session
from database import crud 

router = APIRouter(
    default="/user/",
    tags=["user"]
)

# middle ware
@router.get("/")
async def list_of_user(db:Session= Depends(get_db)):
    return crud.create_user(db=db)

@router.get("/{id}")
async def list_user(id=id, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=id)
    

@router.post("/")
async def get_create_user(user:UserBaseModel, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user) 
        