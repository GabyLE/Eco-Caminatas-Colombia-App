from bson import ObjectId

class PyObjectId(str):  # la clase para que herede de str
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return str(v)  # Convertir el ObjectId a string para almacenamiento