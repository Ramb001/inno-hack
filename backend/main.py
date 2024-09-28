import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import create_tables
from routers import users, organizations

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(organizations.router)

# CORS configuration
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
    logging.info("Starting application...")

    try:
        logging.info("Creating tables...")
        create_tables_result = create_tables()
        if create_tables_result:
            logging.info("Tables created successfully")
        else:
            logging.error("Failed to create tables")
    except Exception as e:
        logging.error(f"An error occurred during startup: {e}")
