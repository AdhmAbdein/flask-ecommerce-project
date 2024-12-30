import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "postgresql://adham:1234@postgres-service-ecommerce/ecommerce_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

