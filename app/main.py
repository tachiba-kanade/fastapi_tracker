"""
Creates FastAPI app                              
Connects all routers

- create  the fastapi app
- register routes
- start the application


"""
from app.core.config import settings
from fastapi import Depends, FastAPI, HTTPException, status
from app.core.database import check_database_connection
from sqlalchemy.exc import SQLAlchemyError

import database_models

app = FastAPI(
    title="Expense tracker",
    description="This is for tracking my personal app",
    version=1.0
)

@app.get("/")
def root():
    return {"The Tracker is up and running"}

@app.get("/health")
def health_check():
    return {
        "Status" : "FASTAPI IS RUNNING OK, ALL GOOD",
        }


@app.get("/db-health")
def db_health():
    try:
        check_database_connection()

        return{
            "Status" : "DATABASE IS RUNNING OK, ALL GOOD",
        }
    except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Database connection failed",
            )
        