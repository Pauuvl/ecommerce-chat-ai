class ProductService:
    """
    Lógica de negocio de productos.
    """

    def __init__(self, repository):
        self.repository = repository

    def get_products(self):
        return self.repository.get_all()

    def get_product_by_id(self, product_id):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise Exception("Producto no encontrado")
        return product