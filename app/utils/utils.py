from datetime import datetime, timedelta
from typing import Union, Any

from fastapi import HTTPException
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from starlette import status

from app.model.account import Account
from app.model.auth import InvalidToken

import os

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
HASH_ALGORITHM = os.getenv('HASH_ALGORITHM')

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 비밀번호 해시처리
def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


# 비밀번호 검증
def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


# 액세스 토큰 생성
def create_access_token(subject: Union[str, Any]) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, HASH_ALGORITHM)
    return encoded_jwt


# 인증 확인 및 사용자 정보 반환
def get_current_account(token: str, db: Session):
    try:
        # 토큰이 아에 없는 경우
        if token == 'null' or token is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='인증되지 않은 사용자입니다.',
            )

        if len(token.split(" ")) == 2:
            token = token.split(" ")[1]

        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[HASH_ALGORITHM]
        )

        # 로그아웃 한 경우
        invalid_token = db.query(InvalidToken).filter(InvalidToken.token == token).first()
        if invalid_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='인증되지 않은 사용자입니다.',
            )

        # 토큰이 있지만 만료된 경우
        if datetime.fromtimestamp(payload['exp']) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='토큰이 만료되었습니다. 다시 로그인 해주세요.',
            )

    # 그 외 jwt 토큰 에러
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='인증되지 않은 사용자입니다.',
        )

    account = db.query(Account).filter(Account.phone == payload['sub']).first()
    return {'account': account, 'token': token}
