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
    def __convert_string_to_datetime(self, value:str):
        if(type(value)!= str ):
            return None 
        try :
            return parser.parse(value)

        except ValueError:
            return None
    
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        

        if(request.method == "GET"):
            response:Response = await call_next(request)
            timezone = request.headers.get("x-timezone", default="UTC")

            try:
                user_tz = pytz.timezone(timezone)
            except pytz.UnknownTimeZoneError:
                user_tz = pytz.UTC 
            
            if(response.status_code == 200 and response.headers.get("content-type") == "application/json"):
                response_body = b""
                async for chunk in response.body_iterator:
                    response_body += chunk
                body = response_body.decode("utf-8")                  
                print("body is " + f"{body}")
                
                
                body = json.loads(body)
                
                for key, value in body.items():
                    pts = self.__convert_string_to_datetime(value)
                    if( pts != None): 
                            new_time_stamp = pts.astimezone(user_tz)
                            body[key] = new_time_stamp
                            print("I come here") 
                
                string_body = json.dumps(body)
                response_body = string_body.encode()

                headers = dict(response.headers)
                print(headers)
                print(headers["content-length"])
                print(len(response_body))
                headers["content-length"] = str(len(response_body))
                return Response(content=response_body, status_code=response.status_code, headers=headers, media_type=response.media_type)
            return response

        return await call_next(request)

    



app.add_middleware(LocalTimeConversionMiddleware)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user.router)
