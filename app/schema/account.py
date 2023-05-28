import datetime

from pydantic import BaseModel
from typing import Optional


# shared properties
class AccountBase(BaseModel):
    is_superuser: bool = False
    update_date: datetime.datetime
    delete_date: datetime.datetime


# Properties to receive via API on creation
class AccountCreate(AccountBase):
    phone: int
    password: str


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
