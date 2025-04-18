from pydantic import BaseModel, Field
from typing import Optional
from models.common import PyObjectId
from bson import ObjectId

class Caminata(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    nombre: str
    kilometros: float
    duracion: str

    class Config:  # esta clase interna configura validaciones y serialización
        validate_by_name = True  # permite usar 'id' en lugar de '_id'
        arbitrary_types_allowed = True         # permite usar tipos como ObjectId
        json_encoders = {
            ObjectId: str                      # convierte ObjectId a string en respuestas JSON
        }