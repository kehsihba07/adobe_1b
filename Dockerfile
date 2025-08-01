FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py"]
