FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
	python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Define la variable de entorno para Flask (sin espacios alrededor de '=')
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
