# import datetime
# from fastapi import Request
# import pytz

# from main import app 


# @app.middleware("http")
# async def add_timezone_header(request: Request, call_next):
#     if request.method == "GET":
#         timezone = request.headers.get("X-Timezone", "UTC")

#         try:


#             user_tz = pytz.timezone(timezone)

#         except pytz.UnknownTimeZoneError:
#             user_tz = pytz.UTC 

#         response = await call_next(request)

#         if response.status_code == 200 and response.headers.get("content-type") == "application/json":
#             body = await response.json()
#             for key, value in body.items():
#                 if "timestamp" in key:
#                     local_time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
#                     utc_time = local_time.astimezone(pytz.UTC)
#                     body[key] = utc_time.isoformat()
#             response.body = body.json().encode("utf-8")
#         return response
#     else:
#         return await call_next(request)  