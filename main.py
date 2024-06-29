from typing import Awaitable, Callable
import pytz
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from app.database import db, models 
from app.router import user
import datetime
from fastapi.responses import JSONResponse 
import json
from dateutil import parser 

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LocalTimeConversionMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        

        if(request.method == "GET"):
            request.headers.get("x-timezone", default="UTC")

        return await call_next(request)

app.add_middleware(LocalTimeConversionMiddleware)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user.router)
