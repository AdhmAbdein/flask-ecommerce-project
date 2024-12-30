FROM python:3.10-slim

WORKDIR /app

COPY ./project-code /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

