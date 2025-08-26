import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env si existe
load_dotenv()


class Settings:
    """Clase para gestionar las configuraciones globales de la aplicación."""

    # Entorno de ejecución: development, staging, production
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # URL del API Gateway
    API_GATEWAY_URL: str = os.getenv("API_GATEWAY_URL", "http://localhost:8000")

    # URLs internas de microservicios (útiles para pruebas, tareas o workers)
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")
    USERS_SERVICE_URL: str = os.getenv("USERS_SERVICE_URL", "http://users:8001")
    PRODUCTS_SERVICE_URL: str = os.getenv("PRODUCTS_SERVICE_URL", "http://products:8002")
    LISTINGS_SERVICE_URL: str = os.getenv("LISTINGS_SERVICE_URL", "http://listings:8003")

    # Seguridad (JWT u otra autenticación)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "cambia_esto_en_produccion")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    # Base de datos (si aplica al microservicio actual)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")

    # Otras configuraciones globales que puedes necesitar
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"


# Instancia global que puedes importar desde cualquier módulo
settings = Settings()
