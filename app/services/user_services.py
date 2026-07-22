"""
AuthService      → registration, login, JWT

UserService      → profile, update account, deactivate account. 
(Get a user profile
Update a user profile
Deactivate an account
Reactivate an account, if allowed
Check whether a user exists)

CategoryService  → category rules

ExpenseService   → expense rules

ReportService    → weekly/monthly calculations

"""

from collections import UserString

from fastapi import HTTPException, status
from httpx import HTTPError
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.core.security import hash_password

from app.schemas.user import UserCreate, UserResponse 
from app.models.user import User

class UserService:
    def __init__(self, session: Session):
        self._db = session

def get_user_by_email(db:Session, email_address:str)->User|None:  
    #this  is for the email we want to search for, so either it returns userObj if the email exist, else none 
    statement = select(User).where(
        User.email_address == email_address
    )

def create_user(db:Session, data:UserCreate)->User:
    existing_user = get_user_by_email(db, data.email_address)

    if existing_user is None:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Email already Exist"

        )
    hash_password = hash_password(
        data.password
    )

    user = User(
        name = data.name,
        email_address = data.email_address,
        hash_password = hash_password
    )
    try: 
        db.add(user)
        db.commit()
        db.refresh(user)

    except IntegrityError:
        db.rollback()
    
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Email already Exsit"
        )
