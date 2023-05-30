## Cafe

### 1. Project Settings

```shell
# project clone
$ git clone git@github.com:hyunwoome/cafe.git

# venv setting
$ cd cafe
$ python3 -m venv venv

# package install
$ pip install -r requirements.txt

# docker build
$ docker build -t fastapi .

# run docker compose
$ docker-compose up

# create database (after connect DB)
$ CREATE DATABASE cafe;

# migration
$ alembic upgrade head
```

### 2. API

- [POST] 회원가입 (`/api/auth/sign-up`)
- [POST] 로그인 (`/api/auth/login`)
- [GET] 로그아웃 (`/api/auth/logout`)