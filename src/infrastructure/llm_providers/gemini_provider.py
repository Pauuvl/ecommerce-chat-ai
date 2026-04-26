import os

class GeminiProvider:

    def generate(self, prompt: str) -> str:
        # 👉 si estamos en testing, NO llama API real
        if os.getenv("TESTING") == "1":
            return "Respuesta de prueba"

        # aquí tu implementación real
        return "Respuesta IA"