import os
import psycopg2
import logging


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS organizations (
            id SERIAL PRIMARY KEY,
            ref_link VARCHAR(255) UNIQUE,
            name VARCHAR(255) NOT NULL,
            owner_id INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS organization_workers (
            organization_id INTEGER NOT NULL,
            role VARCHAR(50),
            worker_id INTEGER NOT NULL,
            PRIMARY KEY (organization_id, worker_id),
            FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS statuses (
        org_id INTEGER NOT NULL,
        status VARCHAR(255),
        PRIMARY KEY (org_id),
        FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            status VARCHAR(255) NOT NULL,
            organization_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deadline DATE,
            workers INTEGER[],
            requested BOOLEAN DEFAULT FALSE,
            verified BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
    )

    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            port="5432",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    try:
                        cur.execute("BEGIN;")
                        cur.execute(command)
                        cur.execute("COMMIT;")
                        logging.info(f"Команда выполнена: {command}")
                    except (psycopg2.DatabaseError, Exception) as error:
                        logging.error(f"Ошибка при выполнении команды: {command}")
                        logging.error(error)
                        cur.execute("ROLLBACK;")

                return True
    except (psycopg2.DatabaseError, Exception) as conn_error:
        logging.error("Ошибка подключения к базе данных")
        logging.error(conn_error)

        return False
