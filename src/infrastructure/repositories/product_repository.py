from src.infrastructure.db.models import ProductModel

class ProductRepository:
    """
    Repositorio encargado del acceso a datos de productos.
    """

    def __init__(self, db):
        """
        Constructor del repositorio.

        Args:
            db: sesión de base de datos
        """
        self.db = db

    def get_all(self):
        """
        Obtiene todos los productos desde la base de datos.

        Returns:
            list: lista de productos
        """
        from src.infrastructure.db.models import ProductModel
        return self.db.query(ProductModel).all()