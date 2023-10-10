CREATE TABLE "USER" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    username VARCHAR(255) UNIQUE,
    password BYTEA,
    phone_number VARCHAR(255),
    address VARCHAR(255),
    is_framer BOOLEAN
);

INSERT INTO "USER" (email, username, password, phone_number, address, is_framer)
VALUES
    ('user1@example.com', 'user1', 'password1', '123-456-7890', '123 Main St', TRUE),
    ('user2@example.com', 'user2', 'password2', '987-654-3210', '456 Elm St', FALSE),
    ('user3@example.com', 'user3', 'password3', '555-555-5555', '789 Oak St', TRUE),
    ('user4@example.com', 'user4', 'password4', '111-222-3333', '101 Pine St', FALSE),
    ('user5@example.com', 'user5', 'password5', '444-777-8888', '202 Maple St', TRUE),
    ('user6@example.com', 'user6', 'password6', '999-888-7777', '303 Birch St', FALSE),
    ('user7@example.com', 'user7', 'password7', '777-888-9999', '404 Cedar St', TRUE),
    ('user8@example.com', 'user8', 'password8', '333-666-9999', '505 Redwood St', FALSE),
    ('user9@example.com', 'user9', 'password9', '222-333-4444', '606 Palm St', TRUE),
    ('user10@example.com', 'user10', 'password10', '888-444-2222', '707 Spruce St', FALSE);
