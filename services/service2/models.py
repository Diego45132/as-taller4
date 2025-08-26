from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

from pydantic import BaseModel
from typing import Optional


Base = declarative_base()

class Item(Base):
    """
    Modelo de datos para un ítem.
    """
    __tablename__ = "items"

   
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}', active={self.is_active})>"



class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True  

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  
