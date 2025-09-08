from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI(title="API Gateway - Mercado de Segunda Mano")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api/v1")

SERVICES = {
    "auth": os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001"),
    "users": os.getenv("USERS_SERVICE_URL", "http://users:8001"),
    "products": os.getenv("PRODUCTS_SERVICE_URL", "http://products:8002"),
    "listings": os.getenv("LISTINGS_SERVICE_URL", "http://listings:8003"),
}

def build_service_url(service_name: str, path: str) -> str:
    return f"{SERVICES[service_name].rstrip('/')}/{path.lstrip('/')}"

async def request_forward(method: str, service_name: str, path: str, request: Request = None):
    if service_name not in SERVICES:
        raise HTTPException(status_code=404, detail=f"Service '{service_name}' not found.")
    service_url = build_service_url(service_name, path)
    try:
        async with httpx.AsyncClient() as client:
            if method == "GET":
                response = await client.get(service_url, params=request.query_params)
            elif method == "POST":
                payload = await request.json()
                response = await client.post(service_url, json=payload)
            elif method == "PUT":
                payload = await request.json()
                response = await client.put(service_url, json=payload)
            elif method == "DELETE":
                response = await client.delete(service_url)
            else:
                raise HTTPException(status_code=405, detail="Method not allowed.")
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"{method} error forwarding to {service_name}: {e}")

@router.get("/{service_name}/{path:path}")
async def forward_get(service_name: str, path: str, request: Request):
    return await request_forward("GET", service_name, path, request)

@router.post("/{service_name}/{path:path}")
async def forward_post(service_name: str, path: str, request: Request):
    return await request_forward("POST", service_name, path, request)

@router.put("/{service_name}/{path:path}")
async def forward_put(service_name: str, path: str, request: Request):
    return await request_forward("PUT", service_name, path, request)

@router.delete("/{service_name}/{path:path}")
async def forward_delete(service_name: str, path: str, request: Request = None):
    return await request_forward("DELETE", service_name, path, request)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API Gateway is running."}

app.include_router(router)
