from fastapi import APIRouter, HTTPException, Body
from models.registro import Registro, RegistroUpdate
from database import registros_collection
from bson import ObjectId

router = APIRouter()


# Registros
# Crear un registro
@router.post("/registros")
def crear_registro(registro: Registro = Body(...)): # body = {fecha_realizacion: date, caminata_id: str, asistentes: list}
    # Convertir la caminata en un diccionario y usar el alias para el _id
    registro_dict = registro.dict(by_alias=True)
    registro_dict.pop("_id", None)  # Remove _id if it's in the dictionary
    # Insertar la caminata en la base de datos
    result = registros_collection.insert_one(registro_dict)
    
    # Retornar un mensaje y el _id del registro creado
    return {"mensaje": "Registro añadido exitosamente", "id": str(result.inserted_id)}

# Obtener lista de registros
@router.get("/registros")
def obtener_registros():
    registros = list(registros_collection.find())  # Obtener los registros desde la base de datos
    
     # Convertir cada documento de MongoDB a un objeto Registro, ignorando valores None
    registros_list = [Registro(**{k: v for k, v in registro.items() if v is not None}) for registro in registros]
    
    return {"registros": registros_list}

# #Obtener registros de una persona por cédula
@router.get("/registros/persona/{cedula}")
def obtener_registros_persona(cedula: str):
    registros_cursor = registros_collection.find({"asistentes": cedula})
    registros = [Registro(**registro) for registro in registros_cursor]

    if not registros:
        raise HTTPException(status_code=404, detail="No se encontraron registros para esta cédula")

    return {"registros": registros}

# Obtener registros de una caminata por id
@router.get("/registros/caminata/{caminata_id}")
def obtener_registros_caminata(caminata_id: str):
    try:
        object_id = ObjectId(caminata_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de caminata no válido")

    registros_cursor = registros_collection.find({"caminata_id": object_id})
    registros = [Registro(**registro) for registro in registros_cursor]

    if not registros:
        raise HTTPException(status_code=404, detail="No se encontraron registros para esta caminata")

    return {"registros": registros}


# Eliminar registro
@router.delete("/registros/{registro_id}")
def eliminar_registro(registro_id: str):
    try:
        object_id = ObjectId(registro_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de registro no válido")
    
    resultado = registros_collection.delete_one({"_id": object_id})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Registro no encontrada")
    
    return {"mensaje": "Registro eliminado"}