FROM python:3.8-slim

WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["opentelemetry-instrument", "python", "app.py"]
