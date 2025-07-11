from pydantic import BaseModel
from typing import Optional

class Ficha(BaseModel):
    id: Optional[str]
    nombre: Optional[str]
    telefono: Optional[str]
    email: Optional[str]
    poblacion: Optional[str]
    grupo_parroquial: Optional[str]
    unidad: Optional[str]
    moderador: Optional[str]
    tel_moderador: Optional[str]
    arciprestazgo: Optional[str]
    arcipreste: Optional[str]
    tel_arciprestazgo: Optional[str]
    animador: Optional[str]
    tel_animador: Optional[str]
