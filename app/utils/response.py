from fastapi.responses import JSONResponse


class Response(JSONResponse):
    def __init__(self, code: int, message: str, data: dict = None, status_code: int = 200, headers=None):
        response_data = {
            "meta": {
                "code": code,
                "message": message
            },
            "data": data
        }
        super().__init__(content=response_data, status_code=status_code, headers=headers)
