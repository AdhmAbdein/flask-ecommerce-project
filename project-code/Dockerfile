FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./project-code /app

RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

EXPOSE 5000

CMD ["sh", "-c", "python init_db.py && python run.py"]

