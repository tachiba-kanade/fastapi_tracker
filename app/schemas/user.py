from datetime import datetime
from argon2 import hash_password
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.mypy import from_attributes_callback
from pytest import Config

class UserCreate(BaseModel): #during the login and registration name , email and address will be send
    name:str = Field(
        min_length=2,
        max_length=150
    )
    email_address:str = EmailStr
    #The client sends a plain password temporarily over the protected HTTP request.
    password:str = Field(
        min_length=8,
        max_length=128,
    )

class UserResponse(BaseModel):
    id: int
    name: str
    email_address: EmailStr
    is_active: bool
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(
        from_attributes=True
    )
