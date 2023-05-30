from passlib.context import CryptContext
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.model.product import Product
from app.schema.product import ProductCreate, ProductUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crud_create_product(db: Session, _product_create: ProductCreate, account_id: int):
    db_product = Product(account_id=account_id,
                         category=_product_create.category,
                         size=_product_create.size,
                         name=_product_create.name,
                         tag=_product_create.tag,
                         price=_product_create.price,
                         cost=_product_create.cost,
                         description=_product_create.description,
                         barcode=_product_create.barcode,
                         expiration_date=_product_create.expiration_date,
                         create_date=func.now()
                         )
    db.add(db_product)
    db.commit()


def crud_update_product(db: Session, _product_update: ProductUpdate, account_id: int, product_id: int):
    product = db.query(Product).filter(
        Product.id == product_id, Product.account_id == account_id, Product.delete_date == None
    ).first()
    if product:
        if _product_update.category:
            product.category = _product_update.category
        if _product_update.size:
            product.size = _product_update.size
        if _product_update.name:
            product.name = _product_update.name
        if _product_update.tag:
            product.tag = _product_update.tag
        if _product_update.price:
            product.price = _product_update.price
        if _product_update.cost:
            product.cost = _product_update.cost
        if _product_update.description:
            product.description = _product_update.description
        if _product_update.barcode:
            product.barcode = _product_update.barcode
        if _product_update.expiration_date:
            product.expiration_date = _product_update.expiration_date
        product.update_date = func.now()
        db.commit()
        db.refresh(product)


def crud_delete_product(db: Session, account_id: int, product_id: int):
    product = db.query(Product).filter(
        Product.id == product_id, Product.account_id == account_id
    ).first()
    if product:
        product.delete_date = func.now()
        db.commit()
        db.refresh(product)


def crud_get_product(db: Session, account_id: int, product_id: int):
    return db.query(Product).filter(
        Product.id == product_id, Product.account_id == account_id
    ).first()


def crud_get_product_list(db: Session, last_seen_id, limit):
    if last_seen_id:
        return db.query(Product).filter(Product.id < last_seen_id).order_by(Product.id.desc()).limit(limit).all()

    return db.query(Product).order_by(Product.id.desc()).limit(limit).all()


def crud_search_product_list(db: Session, search: str):
    product_name = db.query(Product).filter(Product.name.like(f'%{search}%')).all()
    if product_name:
        return product_name
    product_tag = db.query(Product).filter(Product.tag.like(f'%{search}%')).all()
    if product_tag:
        return product_tag
