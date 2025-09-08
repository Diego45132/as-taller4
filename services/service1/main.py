from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Producto
from schemas import ProductoOut, ProductoCreate
from database import get_db, create_db_and_tables

app = FastAPI(
    title="Servicio de Catálogo",
    description="Microservicio para gestionar productos del mercado de segunda mano",
    version="1.0.0"
)

router = APIRouter()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Servicio de catálogo en funcionamiento."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/productos/", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    try:
        productos = db.query(Producto).all()
        return productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al listar productos: {str(e)}")

@router.post("/productos/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    try:
        nuevo_producto = Producto(**producto.dict())
        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)
        return nuevo_producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear producto: {str(e)}")

app.include_router(router, prefix="/api/v1")
