from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class ErrorResponse(BaseModel):
    meta: dict
    data: None = None


async def custom_http_exception_handler(request, exc: HTTPException):
    error_message = exc.detail
    error_response = ErrorResponse(meta={"code": exc.status_code, "message": error_message}, data=None)
    return JSONResponse(content=error_response.dict(), status_code=exc.status_code)
