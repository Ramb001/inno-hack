from pydantic import BaseModel
from typing import List


class Organization(BaseModel):
    id: int
    ref_link: str
    name: str
    owner_id: int


class OrganizationWorker(BaseModel):
    organization_id: int
    role: str
    worker_id: int


class AddOrganization(BaseModel):
    name: str
    ref_link: str
    owner_id: int


class OrganizationWithWorkers(BaseModel):
    organization: Organization
    workers: List[OrganizationWorker]


class Register(BaseModel):
    username: str
    password: str
    email: str
    name: str


class Login(BaseModel):
    username: str
    password: str


class UserOrganization(BaseModel):
    id: int
    name: str
    role: str


class OrganizationWorkerCreate(BaseModel):
    role: str


class Task(BaseModel):
    title: str
    description: str
    status: str
    organization_id: int
    deadline: str
    workers: List[int]


class TaskUpdateStatus(BaseModel):
    status: str


class TaskUpdateDeadline(BaseModel):
    deadline: str


class TaskUpdateWorkers(BaseModel):
    workers: List[int]
