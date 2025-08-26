from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Servicio de Ejemplo",
    description="Microservicio básico para verificación de estado",
    version="1.0.0"
)

@app.get("/health", summary="Verifica el estado del servicio")
async def health_check():
    return JSONResponse(content={"status": "ok"})
