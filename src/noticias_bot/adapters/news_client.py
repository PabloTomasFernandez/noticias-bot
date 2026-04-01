import httpx
from noticias_bot.domain.models import Noticia

class NewsClient:
    """Adapter para conectarse con APIs de noticias externas."""
    
    def __init__(self):
        self.client = httpx.Client() # Cliente síncrono para empezar

    def obtener_noticia_destacada(self) -> Noticia:
        # Por ahora simulamos la respuesta de una API
        return Noticia(
            titulo="IA de Google revoluciona la medicina",
            resumen="Nuevos modelos de lenguaje detectan enfermedades...",
            url="https://ciencia.com/ia-medicina",
            fuente="CienciaHoy"
        )