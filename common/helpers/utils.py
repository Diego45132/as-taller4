import json
import requests
from typing import Any, Optional, Dict
from datetime import datetime


def send_request_to_service(
    url: str,
    method: str = "GET",
    data: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 5
) -> dict:
    """
    Envía una petición HTTP a otro microservicio.

    Args:
        url (str): La URL completa del endpoint.
        method (str): El método HTTP (GET, POST, PUT, DELETE).
        data (Any): Los datos a enviar en el cuerpo de la petición (para POST/PUT).
        headers (Optional[Dict[str, str]]): Cabeceras HTTP opcionales.
        timeout (int): Tiempo máximo de espera en segundos.

    Returns:
        dict: La respuesta del servicio en formato JSON.

    Raises:
        requests.exceptions.RequestException: Si la petición falla.
    """
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            json=data,
            headers=headers,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Falló la petición a {url}: {e}")
        raise e


def format_date(dt_object: datetime) -> str:
    """
    Formatea un objeto datetime a una cadena legible (YYYY-MM-DD HH:MM:SS).

    Args:
        dt_object (datetime): Objeto datetime.

    Returns:
        str: Fecha formateada como cadena.
    """
    return dt_object.strftime("%Y-%m-%d %H:%M:%S")


def parse_date(date_str: str) -> datetime:
    """
    Convierte una cadena de texto a un objeto datetime.

    Args:
        date_str (str): Cadena de fecha en formato 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        datetime: Objeto datetime correspondiente.
    """
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


