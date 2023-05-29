import datetime

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
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


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
