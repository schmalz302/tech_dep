from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.orm import sessionmaker, Session

from models import *

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)


# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

