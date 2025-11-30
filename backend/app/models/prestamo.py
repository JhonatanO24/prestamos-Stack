from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Prestamo(BaseModel):
    usuario_id: str
    libro_id: str
    fecha_prestamo: datetime
    fecha_devolucion_esperada: datetime
    fecha_devolucion_real: Optional[datetime] = None

class PrestamoDB(Prestamo):
    id: Optional[str] = None
