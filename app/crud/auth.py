from passlib.context import CryptContext
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.schema.account import AccountCreate
from app.model.account import Account

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crud_create_account(db: Session, account_create: AccountCreate):
    db_account = Account(phone=account_create.phone,
                         password=pwd_context.hash(account_create.password),
                         create_date=func.now())
    db.add(db_account)
    db.commit()
