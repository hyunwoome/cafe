import datetime
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    update_date: Optional[datetime.datetime]
    delete_date: Optional[datetime.datetime]


class ProductCreate(ProductBase):
    category: str
    size: str
    name: str
    tag: str
    price: int
    cost: int
    description: str
    barcode: str
    expiration_date: datetime.datetime


class ProductUpdate(ProductBase):
    category: Optional[str]
    size: Optional[str]
    name: Optional[str]
    tag: Optional[str]
    price: Optional[int]
    cost: Optional[int]
    description: Optional[str]
    barcode: Optional[str]
    expiration_date: Optional[datetime.datetime]


class ProductInDBBase(ProductBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass


class AccountInDB(ProductInDBBase):
    pass
