from sqlalchemy import Column, Integer, String, Float
from src.infrastructure.db.database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)


class ChatMemoryModel(Base):
    __tablename__ = "chat_memory"

    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    role = Column(String)
    content = Column(String)