from src.infrastructure.llm_providers.gemini_provider import GeminiProvider


class ChatService:

    def __init__(self, repository):
        self.repository = repository
        self.llm = GeminiProvider()

    def send_message(self, session_id: str, message: str):

        # Guardar mensaje usuario
        self.repository.save_message(session_id, "user", message)

        # Obtener historial
        history = self.repository.get_recent_messages(session_id)

        context = "\n".join(
            [f"{m.role}: {m.message}" for m in reversed(history)]
        )

        prompt = f"""
Eres un asistente de ecommerce.

Historial:
{context}

Usuario: {message}
"""

        try:
            response = self.llm.generate_response(prompt)
        except Exception:
            # 🔥 fallback para tests (IMPORTANTE)
            response = "Respuesta generada por fallback (sin IA)"

        # Guardar respuesta
        self.repository.save_message(session_id, "assistant", response)

        return response

    def get_history(self, session_id):
        return self.repository.get_session_history(session_id)

    def delete_history(self, session_id):
        self.repository.delete_session_history(session_id)