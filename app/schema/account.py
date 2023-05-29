import datetime

from fastapi import HTTPException
from pydantic import BaseModel, validator
from typing import Optional


# shared properties
class AccountBase(BaseModel):
    is_superuser: bool = False
    update_date: Optional[datetime.datetime]
    delete_date: Optional[datetime.datetime]


# Properties to receive via API on creation
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
        phone = phone.replace(" ", "") # 공백제거
        if not phone.isdigit() or len(phone) != 11:
            raise HTTPException(status_code=400, detail="유효한 핸드폰 번호를 입력해주세요.")
        return phone


class AccountInDBBase(AccountBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    hashed_password: str
