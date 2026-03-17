ARG PORT=8080

FROM cypress/browsers:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

# ACTUALIZAR HERRAMIENTAS DE BUILD
RUN pip3 install --upgrade pip setuptools wheel --break-system-packages

COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}