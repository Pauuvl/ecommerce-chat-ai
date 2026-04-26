from src.infrastructure.db.models import ChatMemoryModel

class ChatRepository:
    """
    Repositorio para manejar el almacenamiento del historial de chat.
    """

    def __init__(self, db):
        """
        Constructor del repositorio.

        Args:
            db: sesión de base de datos
        """
        self.db = db