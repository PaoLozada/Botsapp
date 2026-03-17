FROM cypress/browsers:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .



CMD echo "PORT=$PORT" && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}