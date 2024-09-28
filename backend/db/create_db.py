import os
import psycopg2


def create_tables():
    commands = (
        """"
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE organizations (
            id SERIAL PRIMARY KEY,
            ref_link VARCHAR(255) UNIQUE,
            name VARCHAR(255) NOT NULL,
            owner_id INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE organization_workers (
            organization_id INTEGER NOT NULL,
            role VARCHAR(50),
            worker_id INTEGER NOT NULL,
            PRIMARY KEY (organization_id, worker_id),
            FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
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
                        print(f"Команда выполнена: {command}")
                    except (psycopg2.DatabaseError, Exception) as error:
                        print(f"Ошибка при выполнении команды: {command}")
                        print(error)
                        cur.execute("ROLLBACK;")
    except (psycopg2.DatabaseError, Exception) as conn_error:
        print("Ошибка подключения к базе данных")
        print(conn_error)
