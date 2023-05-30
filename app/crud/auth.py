from sqlalchemy import func
from sqlalchemy.orm import Session

from app.model.auth import InvalidToken
from app.utils.utils import get_hashed_password
from app.schema.account import AccountCreate
from app.model.account import Account


def crud_create_account(db: Session, account_create: AccountCreate):
    db_account = Account(phone=account_create.phone,
                         password=get_hashed_password(account_create.password),
                         create_date=func.now())
    db.add(db_account)
    db.commit()


def crud_get_existing_account(db: Session, account_create: AccountCreate):
    return db.query(Account).filter(Account.phone == account_create.phone).first()


def crud_get_account(db: Session, phone: str):
    return db.query(Account).filter(Account.phone == phone).first()


def crud_save_token(db: Session, invalid_token: str):
    get_invalid_token = InvalidToken(token=invalid_token.split(" ")[1], create_date=func.now())
    db.add(get_invalid_token)
    db.commit()


def crud_check_invalid_token(db: Session, _token: str):
    return db.query(InvalidToken).filter((InvalidToken.token == _token)).first()
