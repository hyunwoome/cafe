## Cafe

### 1. Stack

- fastapi (python 3.8)
- SQAlchemy (alembic)
- mysql 5.7
- docker, docker compose

### 2. Project Settings

```shell
# .env.sample -> .env
DB_USER=root
DB_PASSWORD=admin
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=cafe

APP_PORT=8080

ACCESS_TOKEN_EXPIRE_MINUTES=10
JWT_SECRET_KEY=4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c
HASH_ALGORITHM=HS256
```

```shell
# project clone
$ git clone git@github.com:hyunwoome/cafe.git

# run docker compose
$ docker-compose up

# fastapi container connect
$ docker exec -it fastapi-container /bin/bash
# migration
$ alembic upgrade head

# running server
http://localhost:8080/
```

### 3. Test

```shell
# account, product 데이터 제거 후 진행

# fastapi container connect
$ docker exec -it fastapi-container /bin/bash
# run test
$ pytest
```

### 4. API

- [POST] 회원 가입 (`/api/auth/sign-up`)
- [POST] 로그인 (`/api/auth/login`)
- [GET] 로그아웃 (`/api/auth/logout`)
- [POST] 상품 생성 (`/api/product`)
- [PATCH] 상품정보 수정 (`/api/product/{product_id}`)
- [DELETE] 상품 삭제 (soft) (`/api/product/{product_id}`)
- [GET] 상품 리스트 조회 (`/api/product/list?last_seen_id=`)
- [GET] 상품 상세 조회 (`/api/product/{product_id}`)
- [GET] 상품 검색 (`/api/product?search=`)


### 5. 보완 사항

- [ ] 일회성 test코드 고도화 (mock 사용해서 DB랑 분리)
- [ ] invalid_token 테이블을 redis로 전환

---

- [ERD](https://dbdiagram.io/d/64704de87764f72fcfe1ba35)