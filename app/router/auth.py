from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from starlette import status
from app.utils.utils import verify_password, create_access_token, get_current_account
from app.database import get_db
from app.crud.auth import crud_create_account, crud_get_existing_account, crud_save_token
from app.schema.account import AccountCreate

from app.utils.response import Response

router = APIRouter(
    prefix="/api/auth",
)


# 회원가입
@router.post('/signup', summary='Create account')
def create_account(_account_create: AccountCreate, db: Session = Depends(get_db)):
    account = crud_get_existing_account(db, _account_create)
    if account:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='이미 계정이 존재합니다.')
    crud_create_account(db=db, account_create=_account_create)
    return Response(code=status.HTTP_200_OK, message='ok', data=None)


# 로그인
@router.post("/login", summary='Create access token')
def login_for_access_token(_account_create: AccountCreate,
                           db: Session = Depends(get_db)):
    account = crud_get_existing_account(db, _account_create)
    if not account or not verify_password(_account_create.password, account.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="핸드폰 번호 및 비밀번호가 일치하지 않습니다.",
        )
    access_token = create_access_token(account.phone)
    data = {"access_token": access_token,
            "token_type": "bearer",
            "phone": account.phone}
    headers = {
        "Authorization": access_token,
    }

    return Response(code=status.HTTP_200_OK, message='ok', data=data, headers=headers)


# 로그아웃
@router.get("/logout", summary='Expired access token')
def logout(authorization: str = Header(default=None), db: Session = Depends(get_db)):
    token = get_current_account(authorization, db=db)['token']
    crud_save_token(db, token)
    return Response(code=status.HTTP_200_OK, message='ok', data=None)
