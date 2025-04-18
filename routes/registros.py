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

# # Obtener lista de caminatas
# @router.get("/caminatas")
# def obtener_caminatas():
#     caminatas = list(caminatas_collection.find())  # Obtener las caminatas desde la base de datos
    
#      # Convertir cada documento de MongoDB a un objeto Caminata, ignorando valores None
#     caminatas_list = [Caminata(**{k: v for k, v in caminata.items() if v is not None}) for caminata in caminatas]
    
#     return {"caminatas": caminatas_list}

# # #Obtener caminata por nombre
# @router.get("/caminatas/{nombre}")
# def obtener_caminata(nombre: str):
#     caminata = caminatas_collection.find_one({"nombre": nombre})
#     if caminata:
#         return Caminata(**caminata)
#     else:
#         raise HTTPException(status_code=404, detail="Caminata no encontrada")

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