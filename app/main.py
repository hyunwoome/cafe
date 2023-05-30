from fastapi import FastAPI
from app.router import auth, product
from app.utils.error_response import custom_http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(default_timezone='Asia/Seoul')


app.include_router(auth.router)
app.include_router(product.router)

app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)