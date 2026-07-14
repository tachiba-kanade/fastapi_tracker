# contain the session connections with postgres


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker