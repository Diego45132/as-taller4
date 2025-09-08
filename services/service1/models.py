from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class Producto(Base):
    """
    Modelo de datos para un producto en el mercado de segunda mano.
    """
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True, nullable=False)
    descripcion = Column(String(500), nullable=True)
    precio = Column(Integer, nullable=False, default=0)  
    disponible = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})>"


class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: int
    disponible: Optional[bool] = True

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
