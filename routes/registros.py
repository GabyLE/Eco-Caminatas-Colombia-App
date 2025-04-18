from fastapi import APIRouter, HTTPException, Body
from models.registro import Registro, RegistroUpdate
from database import registros_collection

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

# # Actualizar caminata
# @router.put("/caminatas/{nombre}")
# def actualizar_caminata(nombre: str, datos_actualizados: CaminataUpadate):
#     actualizacion = {k: v for k, v in datos_actualizados.dict().items() if v is not None}
#     if not actualizacion:
#         raise HTTPException(status_code=400, detail="No se proporcionaron campos a actualizar")

#     resultado = caminatas_collection.update_one({"nombre": nombre}, {"$set": actualizacion})
#     if resultado.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Caminata no encontrada")

#     return {"mensaje": "Caminata actualizada"}

# # Eliminar caminata
# @router.delete("/caminatas/{nombre}")
# def eliminar_caminata(nombre: str):
#     resultado = caminatas_collection.delete_one({"nombre": nombre})
#     if resultado.deleted_count == 0:
#         raise HTTPException(status_code=400, detail="Caminata no encontrada")
#     return {"mensaje": "Caminata eliminada"}