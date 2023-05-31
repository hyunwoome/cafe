import datetime

from fastapi import HTTPException
from pydantic import BaseModel, validator
from typing import Optional


class AccountBase(BaseModel):
    is_superuser: bool = False
    update_date: Optional[datetime.datetime]
    delete_date: Optional[datetime.datetime]


class AccountCreate(AccountBase):
    phone: str
    password: str

    @validator('phone', 'password')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise HTTPException(status_code=400, detail="빈 값이 들어올 수 없습니다.")
        return v

    @validator('phone')
    def validate_phone(cls, phone):
        phone = phone.replace(" ", "")
        if not phone.isdigit() or len(phone) != 11:
            raise HTTPException(status_code=400, detail="유효한 핸드폰 번호를 입력해주세요.")
        return phone


class AccountInDBBase(AccountBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Account(AccountInDBBase):
    pass


class AccountInDB(AccountInDBBase):
    hashed_password: str
