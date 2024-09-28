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
        return {"message": "User registered successfully", "status": "success"}
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return {"message": "User registered failed", "status": "error"}


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
                    SELECT username, name, email FROM users WHERE username = %s AND password = %s
                """,
                    (user.username, user.password),
                )
                result = cur.fetchone()
                if result:
                    username, name, email = result
                    return {
                        "message": "Login successful",
                        "status": "success",
                        "username": username,
                        "name": name,
                        "email": email,
                    }
                else:
                    return {
                        "message": "Login failed",
                        "status": "error",
                    }
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return {
            "message": "Login failed",
            "status": "error",
        }
