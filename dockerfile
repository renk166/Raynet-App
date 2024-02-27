FROM python:3

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir Flask redis

CMD ["python", "app.py"]
