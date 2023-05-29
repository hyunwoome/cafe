from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func, Boolean
from sqlalchemy.orm import relationship
from app.model.product import Product
from app.database import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, autoincrement=True, primary_key=True)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)
    delete_date = Column(DateTime, nullable=True)

    products = relationship("Product", back_populates="account")
