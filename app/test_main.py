from fastapi.testclient import TestClient
from starlette import status

from .main import app

client = TestClient(app)

authorization_header = ''


def test_create_account():
    response = client.post(
        '/api/auth/signup',
        json={'phone': '01072574267', 'password': '13201320'},
    )
    assert response.status_code == status.HTTP_200_OK


def test_login_for_access_token():
    global authorization_header
    response = client.post(
        '/api/auth/login',
        json={'phone': '01072574267', 'password': '13201320'},
    )
    authorization_header = response.headers.get('authorization')
    assert response.status_code == status.HTTP_200_OK


def test_create_product():
    global authorization_header
    response = client.post(
        '/api/product',
        json={
            "category": "음료",
            "size": "M",
            "name": "뜨거운 아메리카노 테스트",
            "tag": "ㄸㄱㅇ,ㅇㅁㄹㅋㄴ",
            "price": 3000,
            "cost": 1000,
            "description": "뜨거운 아메리카노입니다.",
            "barcode": 123412341234,
            "expiration_date": "2023-10-10 00:00:00"
        },
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_update_product():
    global authorization_header
    response = client.patch(
        '/api/product/1',
        json={
            "category": "커피",
        },
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_delete_product():
    global authorization_header
    response = client.delete(
        '/api/product/1',
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_get_product_list():
    global authorization_header
    response = client.get(
        '/api/product/list',
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_get_product():
    global authorization_header
    response = client.get(
        '/api/product/1',
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_search_product():
    global authorization_header
    response = client.get(
        '/api/product',
        params={'search': 'ㄸㄱㅇ'},
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK


def test_logout():
    global authorization_header
    response = client.get(
        '/api/auth/logout',
        headers={"Authorization": authorization_header}
    )
    assert response.status_code == status.HTTP_200_OK
