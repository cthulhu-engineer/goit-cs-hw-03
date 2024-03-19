-- Створення таблиці користувачів
CREATE TABLE users (
                       id SERIAL PRIMARY KEY,
                       fullname VARCHAR(100) NOT NULL,
                       email VARCHAR(100) UNIQUE NOT NULL
);

-- Створення таблиці статусів
CREATE TABLE status (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) UNIQUE NOT NULL
);

-- Створення таблиці завдань
CREATE TABLE tasks (
                       id SERIAL PRIMARY KEY,
                       title VARCHAR(100) NOT NULL,
                       description TEXT,
                       status_id INTEGER NOT NULL,
                       user_id INTEGER NOT NULL,
                       FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE CASCADE,
                       FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
