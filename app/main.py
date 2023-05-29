from fastapi import FastAPI

from app.router import auth

app = FastAPI()

app.include_router(auth.router)
