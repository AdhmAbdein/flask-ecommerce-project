from app import app, db
from models import User, Product, Cart

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if there are any products
        if not Product.query.first():
            # Add some sample products
            products = [
                Product(name='Product 1', price=19.99, description='Description for product 1'),
                Product(name='Product 2', price=29.99, description='Description for product 2'),
                Product(name='Product 3', price=39.99, description='Description for product 3')
            ]
            db.session.add_all(products)
            db.session.commit()

if __name__ == '__main__':
    init_db()

