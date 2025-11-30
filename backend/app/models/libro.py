from pydantic import BaseModel, Field
from typing import Optional

class Libro(BaseModel):
    titulo: str = Field(..., example="Cien años de soledad")
    autor: str = Field(..., example="Gabriel García Márquez")
    disponible: bool = True

class LibroDB(Libro):
    id: Optional[str] = None
