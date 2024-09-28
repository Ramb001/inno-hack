from fastapi import APIRouter, HTTPException
import psycopg2

from src.models import Task

router = APIRouter()


@router.get("/organization/{organization_id}/tasks")
async def get_organization_tasks(organization_id: int):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT t.*, u.username
                    FROM tasks t
                    LEFT JOIN LATERAL unnest(t.workers) worker_id ON true
                    LEFT JOIN users u ON u.id = worker_id
                    WHERE t.organization_id = %s
                """,
                    (organization_id,),
                )
                rows = cur.fetchall()
                tasks = []
                for row in rows:
                    task = {
                        "id": row[0],
                        "title": row[1],
                        "description": row[2],
                        "status": row[3],
                        "organization_id": row[4],
                        "created_at": row[5],
                        "updated_at": row[6],
                        "deadline": row[7],
                        "workers": row[8],
                        "requested": row[9],
                        "verified": row[10],
                        "worker_usernames": [row[11]] if row[11] else [],
                    }
                    # Merge worker usernames for tasks with multiple workers
                    existing_task = next(
                        (t for t in tasks if t["id"] == task["id"]), None
                    )
                    if existing_task:
                        if row[11]:
                            existing_task["worker_usernames"].append(row[11])
                    else:
                        tasks.append(task)
                return tasks
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/organization/{organization_id}/tasks/create")
async def create_organization_task(organization_id: int, task: Task):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO tasks (title, description, status, organization_id, deadline, workers)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING id
                """,
                    (
                        task.title,
                        task.description,
                        task.status,
                        organization_id,
                        task.deadline,
                        task.workers,
                    ),
                )
                task_id = cur.fetchone()[0]
                return {
                    "message": "Task created successfully",
                    "task_id": task_id,
                    "status": "success",
                }
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put("/organization/{organization_id}/tasks/{task_id}/update/status")
async def update_organization_task(organization_id: int, task_id: int, task: Task):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET status = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (task.status, task_id, organization_id),
                )
                return {"message": "Task status updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put("/organization/{organization_id}/tasks/{task_id}/update/deadline")
async def update_organization_task_deadline(
    organization_id: int, task_id: int, task: Task
):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET deadline = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (task.deadline, task_id, organization_id),
                )
                return {"message": "Task deadline updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put("/organization/{organization_id}/tasks/{task_id}/update/workers")
async def update_organization_task_workers(
    organization_id: int, task_id: int, task: Task
):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET workers = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (task.workers, task_id, organization_id),
                )
                return {"message": "Task workers updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.delete("/organization/{organization_id}/tasks/{task_id}/delete")
async def delete_organization_task(organization_id: int, task_id: int):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM tasks
                    WHERE id = %s AND organization_id = %s
                """,
                    (task_id, organization_id),
                )
                return {"message": "Task deleted successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/organization/{organization_id}/tasks/{task_id}/update/request")
async def request_organization_task(organization_id: int, task_id: int, data):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET requested = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (data.requested, task_id, organization_id),
                )
                return {"message": "Task request updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/organization/{organization_id}/tasks/{task_id}/update/verify")
async def verify_organization_task(organization_id: int, task_id: int, task):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET verified = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (task.verified, task_id, organization_id),
                )
                return {"message": "Task verification updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
