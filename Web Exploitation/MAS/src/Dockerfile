FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY flag.txt flag-bde43b3ef8a562d8cdecd767d6c60430.txt

EXPOSE 8002

CMD ["python", "app.py"] 