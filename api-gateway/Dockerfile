# Usa una imagen base ligera de Python 3.12
FROM python:3.12-slim

# Evita preguntas interactivas y reduce tamaño de capa
ENV DEBIAN_FRONTEND=noninteractive

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias del sistema necesarias para compilar algunos paquetes
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente de la aplicación
COPY . .

# Expone el puerto 8000 para que sea accesible externamente
EXPOSE 8000

# Define el comando por defecto para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
