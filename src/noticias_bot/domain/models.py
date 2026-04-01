from pydantic import BaseModel, Field
from datetime import datetime


class Noticia(BaseModel):
    """Representa una noticia procesada por el bot con validación Pydantic."""

    titulo: str = Field(description="El titular de la noticia")
    resumen: str = Field(description="Un resumen de máximo 2 párrafos")
    url: str = Field(description="Link a la fuente original")
    fuente: str = Field(description="Nombre del medio de comunicación")
    fecha_procesada: datetime = Field(default_factory=datetime.now)
