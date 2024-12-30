import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "postgresql://adham:1234@postgres-service-ecommerce/ecommerce_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Define your models
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(255))

# Create tables in the database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
