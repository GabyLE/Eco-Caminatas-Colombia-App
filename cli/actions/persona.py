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
    

def editar_persona():
    return

def eliminar_persona():
    return

def listar_personas():
    return