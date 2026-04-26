from dataclasses import dataclass

@dataclass
class Product:
    """
    Entidad que representa un producto del dominio.
    """

    def __init__(self, name, description, price, stock):
        """
        Constructor de la entidad producto.

        Args:
            name (str): nombre del producto
            description (str): descripción
            price (float): precio
            stock (int): cantidad disponible
        """
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

@dataclass
class ChatMessage:
    session_id: str
    role: str
    content: str


@dataclass
class ChatContext:
    session_id: str
    messages: list