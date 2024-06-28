from pydantic import BaseModel 


class UserBaseModel(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True 