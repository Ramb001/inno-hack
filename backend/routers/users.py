import aiohttp
from fastapi import APIRouter, HTTPException
import psycopg2
import os

from src.models import Register, Login

router = APIRouter()


@router.post("/users/register", tags=["users"])
async def create_user(user: Register):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
            port="5432",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO users (username, password, email, name)
                    VALUES (%s, %s, %s, %s)
                """,
                    (user.username, user.password, user.email, user.name),
                )
                conn.commit()
        return {"message": "User registered successfully"}
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/users/login", tags=["users"])
async def login_user(user: Login):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
            port="5432",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM users WHERE username = %s AND password = %s
                """,
                    (user.username, user.password),
                )
                result = cur.fetchone()
                if result:
                    return {"message": "Login successful"}
                else:
                    raise HTTPException(status_code=401, detail="Invalid credentials")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        raise HTTPException(status_code=500, detail="Internal server error")
