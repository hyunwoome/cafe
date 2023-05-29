from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.utils.response import Response
from app.crud.auth import crud_create_account
from app.schema.account import AccountCreate

router = APIRouter(
    prefix="/api/auth",
)


@router.post("/sign-up", status_code=status.HTTP_204_NO_CONTENT)
def create_account(_account_create: AccountCreate, db: Session = Depends(get_db)):
    crud_create_account(db=db, account_create=_account_create)
    # return Response(code=200, message='OK', data={'sample': 'now'})