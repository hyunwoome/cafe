from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    phone = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    account_status_id = Column(Integer, ForeignKey("account_status.id"))
    account_type_id = Column(Integer, ForeignKey("account_type.id"))
    account_status = relationship("AccountStatus", backref="account")
    account_type = relationship("AccountType", backref="account")
    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)
    delete_date = Column(DateTime, nullable=True)


class AccountStatus(Base):
    __tablename__ = "account_status"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class AccountType(Base):
    __tablename__ = "account_type"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    account_id = relationship("Account", backref="product")
    category_id = relationship("Category", backref="product")
    size_id = relationship("Size", backref="product")
    account = Column(Integer, ForeignKey("account.id"))
    category = Column(Integer, ForeignKey("category.id"))
    size = Column(Integer, ForeignKey("size.id"))
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    barcode = Column(String, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)
    delete_date = Column(DateTime, nullable=True)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Size(Base):
    __tablename__ = "size"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
