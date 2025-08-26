from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)

API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://localhost:8000")

@app.route("/")
def index():
    """Ruta de la página de inicio."""
    try:
        response = requests.get(f"{API_GATEWAY_URL}/api/v1/items")
        response.raise_for_status()  
        items = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el API Gateway: {e}")
        items = []

    return render_template("index.html", title="Inicio", items=items)

@app.route("/new-item", methods=["GET", "POST"])
def new_item():
    """Ruta para crear un nuevo ítem."""
    if request.method == "POST":
        item_data = {
            "name": request.form.get("name"),
            "description": request.form.get("description")
        }

        try:
            response = requests.post(f"{API_GATEWAY_URL}/api/v1/items", json=item_data)
            response.raise_for_status()
            return redirect(url_for("index"))
        except requests.exceptions.RequestException as e:
            print(f"Error al crear el ítem: {e}")
            return "Error al crear el ítem.", 500

    return render_template("form.html", title="Nuevo Ítem")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
