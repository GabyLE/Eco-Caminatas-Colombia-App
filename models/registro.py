from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, List
from models.common import PyObjectId
from datetime import datetime


# El modelo Registro
class Registro(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    fecha_realizacion: datetime
    caminata_id: PyObjectId
    asistentes: List[str]

    class Config:
        validate_by_name = True  # Permite usar 'id' en lugar de '_id'
        arbitrary_types_allowed = True  # Permite tipos personalizados como PyObjectId
        json_encoders = {
            ObjectId: str  # Convierte automáticamente los ObjectId a str en la serialización
        }

class RegistroUpdate(BaseModel):
    fecha_realizacion: Optional[datetime]
    caminata_id: Optional[PyObjectId]
    asistentes: Optional[List[str]]