import aiohttp
from fastapi import APIRouter
import psycopg2

from src.models import Register, Login

router = APIRouter()


@router.post("/users/register", tags=["users"])
async def create_user(user: Register):
    try:
        with psycopg2.connect(
            database="postgres", user="postgres", host="127.0.0.1", password="postgres"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO users (username, password, email, name)
                    VALUES (%s, %s, %s, %s)
                """,
                    (user.username, user.password, user.email, user.name),
                )
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        cur.execute("ROLLBACK;")


@router.post("/users/login", tags=["users"])
async def login_user(user: Login):
    try:
        with psycopg2.connect(
            database="postgres", user="postgres", host="127.0.0.1", password="postgres"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM users WHERE username = %s AND password = %s
                """,
                    (user.username, user.password),
                )
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        cur.execute("ROLLBACK;")
