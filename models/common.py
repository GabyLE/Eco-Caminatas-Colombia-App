from bson import ObjectId
from bson.errors import InvalidId

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
