from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""
Configuración de la base de datos usando SQLAlchemy.
"""

DATABASE_URL = "sqlite:///./data/ecommerce_chat.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    """
    Genera una sesión de base de datos para cada request.

    Yields:
        Session: sesión activa de base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()