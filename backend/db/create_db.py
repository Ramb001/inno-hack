import os
import psycopg2


def create_tables():
    commands = (
        # sql запрос на создание таблиц бд
    )

    try:
        with psycopg2.connect(
            database="postgres", user="postgres", host="127.0.0.1", password="postgres"
        ) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    try:
                        cur.execute("BEGIN;")
                        cur.execute(command)
                        cur.execute("COMMIT;")
                    except (psycopg2.DatabaseError, Exception) as error:
                        print(f"Ошибка при выполнении команды: {command}")
                        print(error)
                        cur.execute("ROLLBACK;")
    except (psycopg2.DatabaseError, Exception) as conn_error:
        print("Ошибка подключения к базе данных")
        print(conn_error)
