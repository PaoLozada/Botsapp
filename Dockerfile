FROM cypress/browsers:latest

# 1. Actualizar e instalar python y pip en un solo paso para evitar errores de localización
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 2. Configurar el directorio de trabajo
WORKDIR /app

# 3. Copiar y instalar dependencias de Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código
COPY . .

# 5. Configurar el PATH (si es necesario para scripts locales)
ENV PATH /home/root/.local/bin:${PATH}

# 6. Ejecutar la aplicación usando la variable PORT de Railway
# No definas ARG PORT=443, deja que Railway pase la suya.
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}