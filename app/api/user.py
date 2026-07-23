# from typing import Annotated

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app.core.database import get_db
# from app.models.user import User
# from app.schemas.auth import LoginRequest, TokenRequest
# from app.schemas.user import UserCreate, UserResponse
# from app.services.user_services import authenticate_user, create_user


# router = APIRouter(
#     prefix="/users",
#     tags=["Users"],
# )


# @router.post(
#     "/register",
#     response_model=UserResponse,
#     status_code=status.HTTP_201_CREATED,
# )
# def register_user(
#     data: UserCreate,
#     db: Annotated[Session, Depends(get_db)],
# ) -> User:
#     return create_user(
#         db=db,
#         data=data,
#     )


# @router.post(
#     "/login",
#     response_model=TokenRequest,
#     status_code=status.HTTP_200_OK,
# )
# def login_user(
#     data: LoginRequest,
#     db: Annotated[Session, Depends(get_db)],
# ) -> TokenRequest:
#     user = authenticate_user(
#         db=db,
#         email_address=str(data.email_address),
#         password=data.password,
#     )

#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid email or password",
#         )

#     return TokenRequest(
#         access_token="temporary-token",
#         token_type="bearer",
#     )

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.user_services import authenticate_user, create_user


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    return create_user(
        db=db,
        data=data,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
def login_user(
    data: LoginRequest,
    db: Annotated[Session, Depends(get_db)],
):
    user = authenticate_user(
        db=db,
        email_address=str(data.email_address),
        password=data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return TokenResponse(
        access_token="temporary-token",
        token_type="bearer",
    )