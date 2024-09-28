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
