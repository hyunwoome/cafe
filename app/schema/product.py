import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class ProductBase(BaseModel):
    update_date: datetime.datetime
    delete_date: datetime.datetime


# Properties to receive via API on creation
class ProductCreate(ProductBase):
    category: str
    size: str
    name: str
    price: int
    cost: int
    description: str
    barcode: str
    expiration_date: datetime.datetime


# Properties to receive via API on update
class ProductUpdate(ProductBase):
    category: str
    size: str
    name: str
    price: int
    cost: int
    description: str
    barcode: str
    expiration_date: datetime.datetime


class ProductInDBBase(ProductBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Product(ProductInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(ProductInDBBase):
    pass
