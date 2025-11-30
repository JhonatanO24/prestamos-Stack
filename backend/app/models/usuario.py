from pydantic import BaseModel, Field
from typing import Optional

class Usuario(BaseModel):
    nombre: str = Field(..., example="Juan Pérez")
    email: str = Field(..., example="juan@email.com")

class UsuarioDB(Usuario):
    id: Optional[str] = None
