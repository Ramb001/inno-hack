from fastapi import APIRouter, HTTPException
from src.models import (
    AddOrganization,
    Organization,
    List,
    OrganizationWithWorkers,
    OrganizationWorker,
    OrganizationWorkerCreate,
)
import psycopg2

router = APIRouter()


@router.post("/organizations/create", tags=["organizations"])
async def add_organization(org: AddOrganization):
    try:
        with psycopg2.connect(
            database="postgres", user="postgres", host="postgres", password="postgres"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO organizations (ref_link, name, owner_id)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                    """,
                    (org.ref_link, org.name, org.owner_id),
                )
                org_id = cur.fetchone()[0]
                conn.commit()
                return {
                    "organization_id": org_id,
                    "message": "Организация успешно создана",
                }
    except (psycopg2.DatabaseError, Exception) as error:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении организации: {str(error)}"
        )


# @router.get("/organizations/organiztion", response_model=List[Organization], tags=["organizations"])
# async def get_organizations():
#     try:
#         with psycopg2.connect(
#             database="postgres", user="postgres", host="postgres", password="postgres"
#         ) as conn:
#             with conn.cursor() as cur:
#                 cur.execute("SELECT id, ref_link, name, owner_id FROM organizations")
#                 rows = cur.fetchall()

#                 organizations = [Organization(id=row[0], ref_link=row[1], name=row[2], owner_id=row[3]) for row in rows]

#                 return organizations
#     except (psycopg2.DatabaseError, Exception) as error:
#         raise HTTPException(status_code=500, detail=f"Ошибка при получении организаций: {str(error)}")


@router.get(
    "/organizations/{organization_id}",
    response_model=OrganizationWithWorkers,
    tags=["organizations"],
)
async def get_organization_with_workers(organization_id: int):
    try:
        with psycopg2.connect(
            database="postgres", user="postgres", host="postgres", password="postgres"
        ) as conn:
            with conn.cursor() as cur:
                # Получаем данные организации
                cur.execute(
                    """
                    SELECT id, ref_link, name, owner_id 
                    FROM organizations 
                    WHERE id = %s
                    """,
                    (organization_id,),
                )
                org_data = cur.fetchone()

                if not org_data:
                    raise HTTPException(
                        status_code=404, detail="Организация не найдена"
                    )

                organization = Organization(
                    id=org_data[0],
                    ref_link=org_data[1],
                    name=org_data[2],
                    owner_id=org_data[3],
                )

                # Получаем работников организации
                cur.execute(
                    """
                    SELECT organization_id, role, worker_id
                    FROM organization_workers
                    WHERE organization_id = %s
                    """,
                    (organization_id,),
                )
                workers_data = cur.fetchall()

                workers = [
                    OrganizationWorker(
                        organization_id=worker[0], role=worker[1], worker_id=worker[2]
                    )
                    for worker in workers_data
                ]

                return OrganizationWithWorkers(
                    organization=organization, workers=workers
                )
    except (psycopg2.DatabaseError, Exception) as error:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при получении организации и её работников: {str(error)}",
        )


@router.post(
    "/organizations/{organization_id}/add/user/{user_id}", tags=["organizations"]
)
async def add_worker_to_organization(
    organization_id: int, user_id: int, data: OrganizationWorkerCreate
):
    try:
        with psycopg2.connect(
            database="postgres",
            user="postgres",
            host="postgres",
            port="5432",
            password="postgres",
        ) as conn:
            with conn.cursor() as cur:
                # Проверяем, существует ли организация
                cur.execute(
                    """
                    SELECT id FROM organizations WHERE id = %s
                    """,
                    (organization_id,),
                )
                org_exists = cur.fetchone()

                if not org_exists:
                    raise HTTPException(
                        status_code=404, detail="Организация не найдена"
                    )

                # Проверяем, существует ли пользователь
                cur.execute(
                    """
                    SELECT id FROM users WHERE id = %s
                    """,
                    (user_id,),
                )
                user_exists = cur.fetchone()

                if not user_exists:
                    raise HTTPException(
                        status_code=404, detail="Пользователь не найден"
                    )

                # Проверяем, не состоит ли пользователь уже в организации
                cur.execute(
                    """
                    SELECT organization_id FROM organization_workers 
                    WHERE organization_id = %s AND worker_id = %s
                    """,
                    (organization_id, user_id),
                )
                existing_worker = cur.fetchone()

                if existing_worker:
                    raise HTTPException(
                        status_code=400,
                        detail="Пользователь уже состоит в этой организации",
                    )

                # Добавляем работника в организацию
                cur.execute(
                    """
                    INSERT INTO organization_workers (organization_id, role, worker_id)
                    VALUES (%s, %s, %s)
                    """,
                    (organization_id, data.role, user_id),
                )
                conn.commit()

                return {"message": "Работник успешно добавлен в организацию"}
    except (psycopg2.DatabaseError, Exception) as error:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении работника: {str(error)}"
        )
