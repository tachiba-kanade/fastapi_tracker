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
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(
    db: Session,
    email_address: str,
) -> User | None:
    statement = select(User).where(
        User.email_address == email_address
    )

    return db.scalar(statement)


def create_user(
    db: Session,
    data: UserCreate,
) -> User:
    email_address = str(data.email_address).lower()

    existing_user = get_user_by_email(
        db=db,
        email_address=email_address,
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    hashed_password = hash_password(data.password)

    user = User(
        name=data.name,
        email_address=email_address,
        hash_password=hashed_password,
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    return user


def authenticate_user(
    db: Session,
    email_address: str,
    password: str,
) -> User | None:
    user = get_user_by_email(
        db=db,
        email_address=email_address.lower(),
    )

    if user is None:
        return None

    if not user.is_active:
        return None

    password_is_correct = verify_password(
        plain_password=password,
        hashed_password=user.hash_password,
    )

    if not password_is_correct:
        return None

    return user