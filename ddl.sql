CREATE TABLE account
(
    id           INT AUTO_INCREMENT
        PRIMARY KEY,
    phone        VARCHAR(20)  NOT NULL,
    password     VARCHAR(100) NOT NULL,
    is_superuser TINYINT(1) NULL,
    create_date  DATETIME     NOT NULL,
    update_date  DATETIME NULL,
    delete_date  DATETIME NULL
);

CREATE TABLE product
(
    id              INT AUTO_INCREMENT
        PRIMARY KEY,
    account_id      INT         NOT NULL,
    category        VARCHAR(10) NOT NULL,
    size            VARCHAR(10) NOT NULL,
    name            VARCHAR(30) NOT NULL,
    tag             TEXT NULL,
    price           INT         NOT NULL,
    cost            INT         NOT NULL,
    description     TEXT        NOT NULL,
    barcode         VARCHAR(50) NOT NULL,
    expiration_date DATETIME    NOT NULL,
    create_date     DATETIME    NOT NULL,
    update_date     DATETIME NULL,
    delete_date     DATETIME NULL,
    CONSTRAINT product_ibfk_1
        FOREIGN KEY (account_id) REFERENCES account (id)
);

CREATE TABLE invalid_token
(
    id          INT AUTO_INCREMENT
        PRIMARY KEY,
    token       VARCHAR(300) NOT NULL,
    create_date DATETIME     NOT NULL
);