from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from models.common import PyObjectId


# El modelo Caminata
class Caminata(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    nombre: str
    kilometros: float
    duracion: str

    class Config:
        validate_by_name = True  # Permite usar 'id' en lugar de '_id'
        arbitrary_types_allowed = True  # Permite tipos personalizados como PyObjectId
        json_encoders = {
            ObjectId: str  # Convierte automáticamente los ObjectId a str en la serialización
        }

class CaminataUpadate(BaseModel):
    nombre: Optional[str]
    kilometros: Optional[float]
    duracion: Optional[str]