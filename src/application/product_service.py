class ProductService:
    """
    Lógica de negocio de productos.
    """

    def __init__(self, repository):
        """
        Constructor del servicio.

        Args:
            repository: repositorio de productos
        """
        self.repository = repository

    def get_products(self):
        """
        Retorna todos los productos.

        Returns:
            list: lista de productos
        """
        return self.repository.get_all()
    