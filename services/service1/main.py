from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database


database.create_db_and_tables()

app = FastAPI(
    title="Servicio de Catálogo",
    description="Microservicio para gestionar productos del mercado de segunda mano",
    version="1.0.0"
)


router = APIRouter()


@app.get("/")
def read_root():
    return {"message": "Servicio de catálogo en funcionamiento."}

@app.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/productos/", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(database.get_db)):
    productos = db.query(models.Producto).all()
    return productos


@router.post("/productos/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    nuevo_producto = models.Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


app.include_router(router, prefix="/api/v1")
