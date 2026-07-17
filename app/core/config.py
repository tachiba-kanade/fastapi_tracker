 # Reads .env settings

# FastAPI → SQLAlchemy → PostgreSQL

"""
1. FastAPI starts - done
2. Configuration loads - done
3. PostgreSQL connects
4. SQLAlchemy models are created
5. Alembic creates tables
6. Pydantic schemas validate data
7. Repository performs queries
8. Service applies rules
9. Router exposes endpoints
10. Authentication is added

"""

"""
.env file
    ↓
config.py reads it
    ↓
settings.database_url
settings.jwt_secret_key

BaseSettings
    = defines and validates your application settings

SettingsConfigDict
    = defines the rules for loading those settings


"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()