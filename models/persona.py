from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ContactoEmergencia(BaseModel):
    nombre: str
    celular: str

class Persona(BaseModel):
    cedula: str = Field(..., alias="_id", description="Número de cédula, usado como ID")
    nombre_completo: str
    celular: str
    correo: EmailStr
    contacto_emergencia: ContactoEmergencia

# Para actualizar
class ContactoEmergenciaUpdate(BaseModel):
    nombre: Optional[str]
    celular: Optional[str]

class PersonaUpdate(BaseModel):
    nombre_completo: Optional[str]
    celular: Optional[str]
    correo: Optional[EmailStr]
    contacto_emergencia: Optional[ContactoEmergenciaUpdate]