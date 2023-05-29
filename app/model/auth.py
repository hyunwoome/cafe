from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class InvalidToken(Base):
    __tablename__ = "invalid_token"

    id = Column(Integer, autoincrement=True, primary_key=True)
    token = Column(String(100), nullable=False)
    create_date = Column(DateTime, nullable=False)
