import aiohttp
from fastapi import APIRouter, HTTPException
import psycopg2
import os
import logging

from src.models import Register, Login, UserOrganization
from typing import List

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
                    RETURNING id;
                """,
                    (user.username, user.password, user.email, user.name),
                )
                user_id = cur.fetchone()[0]
                conn.commit()
        return {
            "message": "User registered successfully",
            "status": "success",
            "user_id": user_id,
            "email": user.email,
        }
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
                    SELECT id, username, name, email FROM users WHERE username = %s AND password = %s
                """,
                    (user.username, user.password),
                )
                result = cur.fetchone()
                if result:
                    id, username, name, email = result
                    return {
                        "message": "Login successful",
                        "status": "success",
                        "username": username,
                        "name": name,
                        "email": email,
                        "user_id": id,
                    }
                else:
                    return {
                        "message": "Login failed",
                        "status": "error",
                    }
    except (psycopg2.DatabaseError, Exception) as error:
        logging.error(error)
        return {
            "message": "Login failed",
            "status": "error",
        }


@router.get(
    "/users/{user_id}/organizations",
    response_model=List[UserOrganization],
    tags=["users"],
)
async def get_user_organizations(user_id: int):
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
                    SELECT o.id, o.name, ow.role
                    FROM organizations o
                    JOIN organization_workers ow ON o.id = ow.organization_id
                    WHERE ow.worker_id = %s
                """,
                    (user_id,),
                )
                rows = cur.fetchall()

                user_organizations = [
                    UserOrganization(id=row[0], name=row[1], role=row[2])
                    for row in rows
                ]

                return user_organizations
    except (psycopg2.DatabaseError, Exception) as error:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving user organizations: {str(error)}"
        )
