from src.infrastructure.llm_providers.gemini_provider import GeminiProvider

class ChatService:
    """
    Servicio encargado de gestionar la interacción con la IA.
    """

    def __init__(self, repository):
        """
        Constructor del servicio.

        Args:
            repository: repositorio de chat
        """
        self.repository = repository
        self.provider = GeminiProvider()

    def send_message(self, session_id: str, message: str):
        """
        Procesa un mensaje del usuario y obtiene respuesta de la IA.

        Args:
            session_id (str): identificador de sesión
            message (str): mensaje del usuario

        Returns:
            str: respuesta de la IA
        """
        response = self.provider.generate(message)
        return response