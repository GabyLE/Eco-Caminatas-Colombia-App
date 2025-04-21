from fastapi import APIRouter, HTTPException, Body, Query
from models.caminata import Caminata, CaminataUpadate
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
@router.get("/caminatas/{nombre}")
def obtener_caminata(nombre: str):
    caminata = caminatas_collection.find_one({"nombre": nombre})
    if caminata:
        return Caminata(**caminata)
    else:
        raise HTTPException(status_code=404, detail="Caminata no encontrada")
    
# Buscar caminata por nombre (coincidencias parciales)
@router.get("/caminatas/buscar/")
def buscar_caminatas(nombre: str = Query(..., description="Nombre a buscar")):
    coincidencias = list(caminatas_collection.find({
        "nombre": {"$regex": nombre, "$options": "i"}
    }))
    
    if not coincidencias:
        raise HTTPException(status_code=404, detail="No se encontraron caminatas con ese nombre")
    
    # Convertir ObjectId a string
    for caminata in coincidencias:
        caminata["_id"] = str(caminata["_id"])

    return {"caminatas": coincidencias}

# Actualizar caminata
@router.put("/caminatas/{nombre}")
def actualizar_caminata(nombre: str, datos_actualizados: CaminataUpadate):
    actualizacion = {k: v for k, v in datos_actualizados.dict().items() if v is not None}
    if not actualizacion:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos a actualizar")

    resultado = caminatas_collection.update_one({"nombre": nombre}, {"$set": actualizacion})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Caminata no encontrada")

    return {"mensaje": "Caminata actualizada"}

# Eliminar caminata
@router.delete("/caminatas/{nombre}")
def eliminar_caminata(nombre: str):
    resultado = caminatas_collection.delete_one({"nombre": nombre})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Caminata no encontrada")
    return {"mensaje": "Caminata eliminada"}