# contain the session connections with postgres
from pydoc import text

from app.core.config import settings


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base, sessionmaker



db_url = settings.database_url


# Manages connections to PostgreSQL.
engine=create_engine(db_url, pool_pre_ping=True)
# pool_pre_ping = SQLAlchemy tests the connection when it is checked out from the pool.
#  If it is dead, SQLAlchemy discards it and reconnects automatically.



# Creates individual database sessions.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# All future SQLAlchemy models will inherit from this class.
class Base(DeclarativeBase):
    pass

# FastAPI will use this to give each request a database session.
"""
db = session(): Initializes a new database session instance.
yield db: Pauses the function and "injects" the active database session into your route or function, allowing you to perform queries.
db.close(): Resumes the function after the request finishes to cleanly close the connection and release it back to the database pool, preventing memory leaks.
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# FastAPI dependencies can use yield to perform cleanup after a request,
# which is why get_db() yields the session and closes it in finally

def check_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))




# Base --> Parent class for future database models
# engine -->	Manages PostgreSQL connections
# SessionLocal	--> Creates database sessions
# get_db()	--> Provides and closes a session for an API request
# check_database_connection()	--> Runs SELECT 1 to test PostgreSQL



#--------------here the models for SLQALCHEMY STARTS---------------------------

# USER