from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request

from app.crud.product import crud_create_product, crud_get_product, crud_delete_product, crud_update_product, \
    crud_get_product_list, crud_search_product_list
from app.database import get_db
from app.schema.product import ProductCreate, ProductUpdate

from app.utils.response import Response
from app.utils.utils import get_current_account

router = APIRouter(
    prefix='/api/product',
)


# 상품 생성
@router.post('', summary='Create product')
def create_product(_product_create: ProductCreate, request: Request, db: Session = Depends(get_db)):
    account = get_current_account(token=request.headers.get('authorization'), db=db)['account']
    crud_create_product(db, _product_create, account.id)
    return Response(code=status.HTTP_200_OK, message='ok', data=None)


# 상품 수정
@router.patch('/{product_id}', summary='Update product')
def update_product(_product_update: ProductUpdate, product_id: int, request: Request, db: Session = Depends(get_db)):
    account = get_current_account(token=request.headers.get('authorization'), db=db)['account']
    crud_update_product(db, _product_update, account.id, product_id)
    return Response(code=status.HTTP_200_OK, message='ok', data=None)


# 상품 삭제 (소프트)
@router.delete('/{product_id}', summary='Delete Product (soft)')
def delete_product(request: Request, product_id: int, db: Session = Depends(get_db)):
    account = get_current_account(token=request.headers.get('authorization'), db=db)['account']
    crud_delete_product(db, account.id, product_id)
    return Response(code=status.HTTP_200_OK, message='ok', data=None)


# 상품 리스트 조회
@router.get('/list', summary='Get product list')
def get_product_list(request: Request, last_seen_id: int = None, limit: int = 10, db: Session = Depends(get_db)):
    get_current_account(token=request.headers.get('authorization'), db=db)
    product_list = crud_get_product_list(db, last_seen_id, limit)
    json_product_list = jsonable_encoder(product_list)
    data = {
        'product_list': json_product_list
    }
    return Response(code=status.HTTP_200_OK, message='ok', data=data)


# 상품 조회
@router.get('/{product_id}', summary='Get product')
def get_product(request: Request, product_id: int, db: Session = Depends(get_db)):
    account = get_current_account(token=request.headers.get('authorization'), db=db)['account']
    product = crud_get_product(db, account.id, product_id)
    json_product = jsonable_encoder(product)
    data = {
        'product': json_product
    }
    return Response(code=status.HTTP_200_OK, message='ok', data=data)


# 상품 검색
@router.get('', summary='Search Product')
def search_product(search: str, request: Request, db: Session = Depends(get_db)):
    get_current_account(token=request.headers.get('authorization'), db=db)
    product = crud_search_product_list(db, search)
    json_product = jsonable_encoder(product)
    data = {
        'product': json_product
    }
    return Response(code=status.HTTP_200_OK, message='ok', data=data)
