# Pydantic models
from pydantic import BaseModel, EmailStr, Field

# we need the email and password

class LoginRequest(BaseModel):
    email_address: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
    )

class TokenRequest(BaseModel):
    access_token: str
    token_type: str = "bearer"
