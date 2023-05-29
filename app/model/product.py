from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    category = Column(String, nullable=False)
    size = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    barcode = Column(String, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)
    delete_date = Column(DateTime, nullable=True)

    account = relationship("Account", back_populates="products")
