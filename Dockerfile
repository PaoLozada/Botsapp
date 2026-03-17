ARG PORT=8080

FROM cypress/browsers:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3.11 python3.11-pip

COPY requirements.txt .

RUN python3.11 -m pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

CMD python3.11 -m uvicorn main:app --host 0.0.0.0 --port ${PORT}