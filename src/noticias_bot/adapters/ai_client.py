import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from noticias_bot.domain.models import Noticia

# Cargamos las variables del .env
load_dotenv()


class AIClient:
    """Adaptador para procesar y resumir noticias usando IA con Structured Outputs."""

    def __init__(self):
        # 1. Inicializamos el cliente de OpenAI (o cualquier provider en 2026)
        # 2. Lo "parcheamos" con Instructor para manejar Pydantic
        self.client = instructor.from_openai(
            OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        )

    def resumir_noticia(self, titulo_original: str, fuente: str) -> Noticia:
        """Usa la IA para generar un resumen estructurado basado en un título."""

        # En 2026, el prompt es el 'contrato' de la tarea
        return self.client.chat.completions.create(
            model="gpt-4o-mini",  # O el modelo que prefieras
            response_model=Noticia,  # <--- La magia de Instructor: valida contra Pydantic
            messages=[
                {
                    "role": "system",
                    "content": "Eres un periodista experto en tecnología. Tu tarea es generar un resumen breve y profesional.",
                },
                {
                    "role": "user",
                    "content": f"Generá una noticia completa para este título: {titulo_original}. Fuente: {fuente}",
                },
            ],
        )
