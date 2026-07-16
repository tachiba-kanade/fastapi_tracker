"""
Creates FastAPI app                              
Connects all routers

- create  the fastapi app
- register routes
- start the application


"""
from app.core.config import settings
from fastapi import Depends, FastAPI

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
        "Status" : "OK, ALL GOOD",
        "database_config": bool(settings.database_url)
        }
    