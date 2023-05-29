from fastapi import FastAPI

from app.router import auth
from app.utils.error_response import custom_http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.include_router(auth.router)

app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
{}