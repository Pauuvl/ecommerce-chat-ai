from src.infrastructure.db.models import ProductModel


class ProductRepository:

    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(ProductModel).all()

    def get_by_id(self, product_id):
        return self.db.query(ProductModel).filter(
            ProductModel.id == product_id
        ).first()

    def save(self, product):
        self.db.add(product)
        self.db.commit()

    def delete(self, product_id):
        product = self.get_by_id(product_id)
        self.db.delete(product)
        self.db.commit()