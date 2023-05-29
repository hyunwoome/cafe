from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Header
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.crud.auth import crud_create_account, crud_get_existing_account, crud_get_account, crud_save_token, \
    crud_check_token
from app.schema.account import AccountCreate

from app.crud.auth import pwd_context
from app.schema.auth import Token
from app.utils.response import Response

ACCESS_TOKEN_EXPIRE_MINUTES = 10
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/auth",
)


@router.post("/sign-up", status_code=status.HTTP_204_NO_CONTENT)
def create_account(_account_create: AccountCreate, db: Session = Depends(get_db)):
    account = crud_get_existing_account(db, _account_create)
    if account:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 번호입니다.")
    crud_create_account(db=db, account_create=_account_create)
    return Response(code=204, message='ok', data=None)


@router.post("/login", response_model=Token)
def login_for_access_token(_account_create: AccountCreate,
                           db: Session = Depends(get_db)):
    account = crud_get_account(db, _account_create.phone)
    if not account or not pwd_context.verify(_account_create.password, account.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="핸드폰 번호 및 비밀번호가 일치하지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {
        "sub": account.phone,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    data = {"access_token": access_token,
            "token_type": "bearer",
            "phone": account.phone}

    headers = {
        "Authorization": access_token,
    }

    return Response(code=200, message='ok', data=data, headers=headers)


@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(authorization: str = Header(default=None), db: Session = Depends(get_db)):
    if crud_check_token(db, authorization):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='인증되지 않은 사용자입니다.')
    crud_save_token(db, authorization)
    return Response(code=200, message='ok')
