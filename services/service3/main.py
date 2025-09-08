from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, create_db_and_tables
from models import YourModel, YourModelCreate, YourModelRead

app = FastAPI(title="Servicio de YourModel")
router = APIRouter()

@app.on_event("startup")
def on_startup():
    """Inicializa la base de datos al iniciar el servicio."""
    create_db_and_tables()

@app.get("/")
def read_root():
    """Endpoint raíz para verificar funcionamiento."""
    return {"message": "Servicio de YourModel en funcionamiento."}

@app.get("/health")
def health_check():
    """Endpoint de salud para verificar el estado del servicio."""
    return {"status": "ok"}

@router.get("/items/", response_model=list[YourModelRead])
def get_items(db: Session = Depends(get_db)):
    """Obtiene todos los items."""
    try:
        return db.query(YourModel).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener items: {str(e)}")

@router.post("/items/", response_model=YourModelRead)
def create_item(item: YourModelCreate, db: Session = Depends(get_db)):
    """Crea un nuevo item."""
    try:
        db_item = YourModel(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear item: {str(e)}")

app.include_router(router, prefix="/api/v1", tags=["items"])
