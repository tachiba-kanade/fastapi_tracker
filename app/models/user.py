# SQLAlchemy models

from datetime import datetime

from argon2 import hash_password
from app.core.database import Base
from sqlalchemy import Boolean, DateTime, String, func, true
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(150), 
        nullable=False)
    
    email_address: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        index=True, 
        nullable=False)

    hash_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False)
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
    Boolean,
    default=True, #is used by SQLAlchemy when Python creates a user.
    server_default=true(), #tells PostgreSQL to use true when an insert does not provide a value.
    nullable=False,
)



