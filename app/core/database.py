# contain the session connections with postgres
# from app.core.config import settings


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

db_url = database_url
engine=create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)