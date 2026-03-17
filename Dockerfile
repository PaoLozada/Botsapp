FROM cypress/browsers:node18.12.0-chrome107

WORKDIR /app

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get update --allow-insecure-repositories && \
    apt-get install -y python3 python3-pip --allow-unauthenticated

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias Python
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Ejecutar la app (el puerto lo maneja main.py)
CMD ["python3", "main.py"]