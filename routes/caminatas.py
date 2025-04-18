from fastapi import APIRouter, HTTPException, Body
from models.caminata import Caminata
from database import caminatas_collection

router = APIRouter()


# CAMINATAS
# Crear una caminata
@router.post("/caminatas")
def crear_caminata(caminata: Caminata = Body(...)):
    # Verificar si la caminata ya existe en la base de datos
    if caminatas_collection.find_one({"nombre": caminata.nombre}):
        raise HTTPException(status_code=400, detail="La caminata ya existe")
    
    # Convertir la caminata en un diccionario y usar el alias para el _id
    caminata_dict = caminata.dict(by_alias=True)
    caminata_dict.pop("_id", None)  # Remove _id if it's in the dictionary
    # Insertar la caminata en la base de datos
    result = caminatas_collection.insert_one(caminata_dict)
    
    # Retornar un mensaje y el _id de la caminata creada
    return {"mensaje": "Caminata creada exitosamente", "id": str(result.inserted_id)}

# Obtener lista de caminatas
@router.get("/caminatas")
def obtener_caminatas():
    caminatas = list(caminatas_collection.find())  # Obtener las caminatas desde la base de datos
    
     # Convertir cada documento de MongoDB a un objeto Caminata, ignorando valores None
    caminatas_list = [Caminata(**{k: v for k, v in caminata.items() if v is not None}) for caminata in caminatas]
    
    return {"caminatas": caminatas_list}

# #Obtener caminata por nombre
@router.get("/caminata/{nombre}")
def obtener_caminata(nombre: str):
    caminata = caminatas_collection.find_one({"nombre": nombre})
    if caminata:
        return Caminata(**caminata)
    else:
        raise HTTPException(status_code=404, detail="Caminata no encontrada")

# # Actualizar persona
# @router.put("/personas/{cedula}")
# def actualizar_persona(cedula: str, datos_actualizados: PersonaUpdate):
#     actualizacion = {k: v for k, v in datos_actualizados.dict().items() if v is not None}
#     if not actualizacion:
#         raise HTTPException(status_code=400, detail="No se proporcionaron campos a actualizar")

#     resultado = personas_collection.update_one({"_id": cedula}, {"$set": actualizacion})
#     if resultado.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Persona no encontrada")

#     return {"mensaje": "Persona actualizada"}

# # Eliminar persona
# @router.delete("/personas/{cedula}")
# def eliminar_persona(cedula: str):
#     resultado = personas_collection.delete_one({"_id": cedula})
#     if resultado.deleted_count == 0:
#         raise HTTPException(status_code=400, detail="Persona no encontrada")
#     return {"mensaje": "Persona eliminada"}