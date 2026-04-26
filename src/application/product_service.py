class ProductService:
    """
    Servicio que contiene la lógica de negocio relacionada con productos.
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
        Obtiene todos los productos desde el repositorio.

        Returns:
            list: lista de productos
        """
        return self.repository.get_all()