from faker import Faker
import psycopg2
import os

fake = Faker()

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='567234',
    host='localhost'
)

cur = conn.cursor()

# Створення статусів
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))

# Створення користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;", (fullname, email))

# Створення завдань
for _ in range(30):
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=200)
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);", (title, description, status_id, user_id))

conn.commit()
cur.close()
conn.close()
