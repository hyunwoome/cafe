## Cafe

### 1. Stack

- fastapi (python 3.8)
- SQAlchemy (alembic)
- mysql 5.7
- docker, docker compose

### 2. Project Settings

```shell
# project clone
$ git clone git@github.com:hyunwoome/cafe.git

# venv setting
$ cd cafe
$ python3 -m venv venv
$ source venv/bin/activate

# package install
$ pip install -r requirements.txt

# run docker compose
$ docker-compose up

# migration
$ alembic upgrade head
```

### 3. Test

```shell
# account, product 데이터 제거 후 진행

# run docker compose
$ docker-compose up

# migration
$ alembic upgrade head

# fastapi container connect
$ docker exec -it fastapi-container /bin/bash

# run pytest
$ pytest
```

### 4. API

- [POST] 회원 가입 (`/api/auth/sign-up`) (관리자로 직접 DB 수정)
- [POST] 로그인 (`/api/auth/login`)
- [GET] 로그아웃 (`/api/auth/logout`)
- [POST] 상품 생성 (`/api/product`)
- [PATCH] 상품정보 수정 (`/api/product/{product_id}`)
- [DELETE] 상품 삭제 (soft) (`/api/product/{product_id}`)
- [GET] 상품 리스트 조회 (`/api/product/list?last_seen_id=`)
- [GET] 상품 상세 조회 (`/api/product/{product_id}`)
- [GET] 상품 검색 (`/api/product?search=`)


### 5. 보완 사항

- [ ] 일회성 test 고도화 (mockdata 사용해서 DB랑 분리)
- [ ] invalid_token 테이블을 redis로 전환
- [ ] 환경 변수 분리