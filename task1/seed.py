from faker import Faker
import psycopg2
from contextlib import contextmanager
import config


fake = Faker("uk_UA")

def log(table):
    def wrapper(fn):
        def inner(*args, **kwargs):
            print(f"Generating seed for {table} table...")
            result = fn(*args, **kwargs)
            print("Done")
            return result
        return inner
    return wrapper


@contextmanager
def connect():
    try:
        conn = psycopg2.connect(
            host=config.POSTGRES_HOST,
            dbname=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
        )
        try:
            yield conn
        finally:
            conn.close()
    except psycopg2.OperationalError as e:
        print(e)

@log("users")
def fill_users(cursor):
    for i in range(config.USER_AMOUNT):
        cursor.execute(
            f"INSERT INTO users (fullname, email) VALUES (%s, %s);",
            (fake.name(), fake.email()),
        )
        if i % (config.USER_AMOUNT // 10) == 0:
            print(".", end="", flush=True)
    
@log("tasks")
def fill_tasks(cursor):
    for i in range(config.USER_AMOUNT * config.TASKS_PER_USER):
        task_data = (
            fake.sentence(nb_words=3),
            fake.text(),
            fake.random.randint(1, config.TASK_STATE_MAX),
            fake.random.randint(1,config.USER_AMOUNT),
        )
        cursor.execute(
            f"INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
            task_data,
        )
        if i % (config.USER_AMOUNT * config.TASKS_PER_USER // 10) == 0:
            print(".", end="", flush=True)


def main(conn):
    with conn.cursor() as cur:
        fill_users(cur)
        fill_tasks(cur)
        conn.commit()


if __name__ == "__main__":
    with connect() as conn:
        main(conn)
