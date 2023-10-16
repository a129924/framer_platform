DROP TABLE IF EXISTS "USER";

CREATE TABLE IF NOT EXISTS "USER" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    username VARCHAR(255) UNIQUE,
    password BYTEA,
    phone_number VARCHAR(255),
    address VARCHAR(255),
    is_framer BOOLEAN
);