import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import create_tables
from routers import users, organizations 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


app = FastAPI()
app.include_router(users.router)
app.include_router(organizations.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    create_tables()
