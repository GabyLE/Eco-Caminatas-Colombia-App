from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, *args):
        try:
            return cls(v)
        except InvalidId:
            raise ValueError(f"{v} is not a valid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(self, cls, field_schema):
        return {"type": "string"}


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