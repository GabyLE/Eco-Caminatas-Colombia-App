from fastapi import APIRouter, HTTPException, Body, Query
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
    if not personas:
        raise HTTPException(status_code=404, detail="No se encontraron personas.")
    return {"personas": personas}

# Obtener persona por cédula
@router.get("/personas/{cedula}")
def obtener_persona(cedula: str):
    persona = personas_collection.find_one({"_id": cedula})
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

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

# Buscar personas por nombre (coincidencias parciales)
@router.get("/personas/buscar/")
def buscar_personas(nombre: str = Query(..., description="Nombre a buscar")):
    coincidencias = list(personas_collection.find({
        "nombre_completo": {"$regex": nombre, "$options": "i"}
    }))
    
    if not coincidencias:
        raise HTTPException(status_code=404, detail="No se encontraron personas con ese nombre")
    
    return {"personas": coincidencias}