FROM python:3.8-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask requests

EXPOSE 8080

CMD ["python", "frontend_app.py"]
