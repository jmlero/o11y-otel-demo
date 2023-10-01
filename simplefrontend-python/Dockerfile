FROM python:3.8-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask requests opentelemetry-instrumentation opentelemetry-exporter-otlp opentelemetry-instrumentation-flask

EXPOSE 8080

CMD ["opentelemetry-instrument", "python", "app.py"]
