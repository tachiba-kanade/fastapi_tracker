from fastapi import APIRouter, Depends, HTTPException
from pytest import Session
from sqlalchemy.orm import sessionmaker
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
# from app.services.user_service import UserService


router = APIRouter()

def get_user_service() -> UserService:
    return UserService(session=SessionLocal())

@router.get("/users", response_model=list[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.post("/user_create", response_model=list[UserResponse])
def create_users(user: UserCreate = Depends(UserCreate)):
    return schemas.