from fastapi import APIRouter, HTTPException, Body
from models.persona import Persona, PersonaUpdate
from database import personas_collection

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Eco Caminatas Colombia"}


# PERSONA
# Crear una persona
@router.post("/personas")
def crear_persona(persona: Persona = Body(...)):
    if personas_collection.find_one({"_id": persona.cedula}):
        raise HTTPException(status_code = 400, detail= "La persona ya existe")
    
    persona_dict = persona.dict(by_alias=True)
    persona_dict["caminatas_asistidads"] = [] # Se añade este campo al guardar

    personas_collection.insert_one(persona_dict)
    return {"mensaje": "Persona creada exitosamente"}

# Obtener lista personas
@router.get("/personas")
def obtener_personas():
    personas = list(personas_collection.find())
    return {"personas": personas}

# Obtener persona por cédula
@router.get("/personas/{cedula}")
def obtener_persona(cedula: str):
    persona = personas_collection.find_one({"_id": cedula})
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona["_id"] = str(persona["_id"])
    return persona

# Actualizar persona
@router.put("/personas/{cedula}")
def actualizar_persona(cedula: str, datos_actualizados: PersonaUpdate):
    actualizacion = {k: v for k, v in datos_actualizados.dict().items() if v is not None}
    if not actualizacion:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos a actualizar")

    resultado = personas_collection.update_one({"_id": cedula}, {"$set": actualizacion})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    return {"mensaje": "Persona actualizada"}

# Eliminar persona
@router.delete("/personas/{cedula}")
def eliminar_persona(cedula: str):
    resultado = personas_collection.delete_one({"_id": cedula})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Persona no encontrada")
    return {"mensaje": "Persona eliminada"}