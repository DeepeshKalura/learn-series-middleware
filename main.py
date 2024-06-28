from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import models, database 
from app.router import user

models.Base.metadata.create_all(blind=database.engine)

# dababase dependencies
def get_db():
    db = database.local_session()
    try:
        yield db 
    finally:
        db.close()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route(user)

@app.get("/")
def read_root():
    return {"Hello": "World"}

