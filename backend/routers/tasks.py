from fastapi import APIRouter, HTTPException
import psycopg2
from utils import create_task_notification, update_task_status_notification
from src.models import (
    Task,
    TaskUpdateStatus,
    TaskUpdateDeadline,
    TaskUpdateWorkers,
    TaskUpdateRequest,
    TaskUpdateVerify,
)

from utils import EmailNotificatior

router = APIRouter()


@router.get("/organization/{organization_id}/tasks", tags=["tasks"])
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
                        "requested": row[9],
                        "verified": row[10],
                        "workers": [{"name": row[11]}] if row[11] else [],
                    }
                    # Merge workers for tasks with multiple workers
                    existing_task = next(
                        (t for t in tasks if t["id"] == task["id"]), None
                    )
                    if existing_task:
                        if row[11]:
                            existing_task["workers"].append({"name": row[11]})
                    else:
                        tasks.append(task)
                return tasks
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.post("/organization/{organization_id}/tasks/create", tags=["tasks"])
async def create_organization_task(organization_id: int, task: Task):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                # Проверка, существует ли организация
                cur.execute(
                    """
                    SELECT id FROM organizations WHERE id = %s
                    """,
                    (organization_id,),
                )
                if cur.fetchone() is None:
                    raise HTTPException(status_code=404, detail="Organization not found")

                # Вставка задачи
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

                # Получение email'ов работников
                emails = []
                for worker in task.workers:
                    cur.execute(
                        """
                        SELECT u.email
                        FROM users u
                        WHERE id = %s
                        """,
                        (worker,),
                    )
                    row = cur.fetchone()
                    if row:  # Проверяем, что строка найдена
                        emails.append(row[0])

                # Создание и отправка уведомления
                msg = create_task_notification(task.title, task.description, task.deadline)
                email_notification = EmailNotificatior(
                    receivers=emails,
                    message=msg
                )
                email_notification.send_email('Новая задача создана!')
                return {
                    "message": "Task created successfully",
                    "task_id": task_id,
                    "status": "success",
                }
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put(
    "/organization/{organization_id}/tasks/{task_id}/update/status", tags=["tasks"]
)
async def update_organization_task(
    organization_id: int, task_id: int, data: TaskUpdateStatus
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
                    SET status = %s
                    WHERE id = %s AND organization_id = %s
                    RETURNING title;
                    """,
                    (data.status, task_id, organization_id),
                )
                task_title  = cur.fetchone()[0]

                cur.execute(
                    """
                    SELECT u.email
                    FROM tasks t
                    JOIN organization_workers ow ON ow.organization_id = t.organization_id
                    JOIN users u ON u.id = ow.worker_id
                    WHERE t.id = %s;
                    """,
                    (task_id,),
                )
                
                emails = cur.fetchall()
                emails = [email[0] for email in cur.fetchall()]

                msg = update_task_status_notification(task_title, data.status)
                email_notification = EmailNotificatior(
                    receivers=emails,
                    message=msg
                )
                email_notification.send_email('Новая задача создана!')
                return {"message": "Task status updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put(
    "/organization/{organization_id}/tasks/{task_id}/update/deadline", tags=["tasks"]
)
async def update_organization_task_deadline(
    organization_id: int, task_id: int, data: TaskUpdateDeadline
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
                    (data.deadline, task_id, organization_id),
                )
                return {"message": "Task deadline updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put(
    "/organization/{organization_id}/tasks/{task_id}/update/workers", tags=["tasks"]
)
async def update_organization_task_workers(
    organization_id: int, task_id: int, data: TaskUpdateWorkers
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
                    (data.workers, task_id, organization_id),
                )
                return {"message": "Task workers updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.delete("/organization/{organization_id}/tasks/{task_id}/delete", tags=["tasks"])
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


@router.put(
    "/organization/{organization_id}/tasks/{task_id}/update/requested", tags=["tasks"]
)
async def request_organization_task(
    organization_id: int, task_id: int, data: TaskUpdateRequest
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
                    SET requested = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (data.requested, task_id, organization_id),
                )
                return {"message": "Task request updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.put(
    "/organization/{organization_id}/tasks/{task_id}/update/verified", tags=["tasks"]
)
async def verify_organization_task(
    organization_id: int, task_id: int, data: TaskUpdateVerify
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
                    SET verified = %s
                    WHERE id = %s AND organization_id = %s
                """,
                    (data.verified, task_id, organization_id),
                )
                return {"message": "Task verification updated successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
