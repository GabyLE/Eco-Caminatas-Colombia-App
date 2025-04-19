import requests

def añadir_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer):
    
    response = requests.post("http://127.0.0.1:8000/personas", 
                             json={
                                "_id": cedula,
                                "nombre_completo": nombre,
                                "celular": celular,
                                "correo": correo,
                                "contacto_emergencia": {
                                    "nombre": nombre_contemer,
                                    "celular": celular_contemer
                                }
                                })
    if response.status_code == 200:
        print("Persona añadida con éxito.")
    else:
        print("Error al añadir la persona.")
    
def obtener_persona(cedula):
    response = requests.get("http://127.0.0.1:8000/personas/" + cedula)
    datos = response.json()  # Esto convierte el JSON a un diccionario de Python
    if response.status_code == 200:
        print("Datos actuales:")
        print("Nombre: ", datos["nombre_completo"])
        print("Cédula:", datos["_id"])
        print("Celular: ", datos["celular"])
        print("Correo: ", datos["correo"])
        print("Nombre contacto de emergencia: ", datos["contacto_emergencia"]["nombre"])
        print("Celular contacto de emergencia: ", datos["contacto_emergencia"]["celular"])
    else:
        print(datos["detail"])

def editar_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer):
    response = requests.put("http://127.0.0.1:8000/personas/" + cedula, 
                             json={
                                "nombre_completo": nombre,
                                "celular": celular,
                                "correo": correo,
                                "contacto_emergencia": {
                                    "nombre": nombre_contemer,
                                    "celular": celular_contemer
                                }
                                })
    if response.status_code == 200:
        print("Persona actualizada con éxito.")
    else:
        print("Error al actualizar la persona.")
    return

def eliminar_persona():
    return

def listar_personas():
    return