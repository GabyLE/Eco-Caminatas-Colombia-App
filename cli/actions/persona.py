import requests

def añadir_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/personas", 
            json={
                "_id": cedula,
                "nombre_completo": nombre,
                "celular": celular,
                "correo": correo,
                "contacto_emergencia": {
                    "nombre": nombre_contemer,
                    "celular": celular_contemer
                }
            }
        )

        if response.status_code == 200:
            print("Persona añadida con éxito.")
        elif response.status_code == 400:
            print(f"No se pudo añadir la persona: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")
    
def obtener_persona(cedula):
    try:
        response = requests.get("http://127.0.0.1:8000/personas/" + cedula)

        if response.status_code == 200:
            datos = response.json()
            print("Datos actuales:")
            print("Nombre: ", datos["nombre_completo"])
            print("Cédula:", datos["_id"])
            print("Celular: ", datos["celular"])
            print("Correo: ", datos["correo"])
            print("Nombre contacto de emergencia: ", datos["contacto_emergencia"]["nombre"])
            print("Celular contacto de emergencia: ", datos["contacto_emergencia"]["celular"])
            return True  # Indicador de que fue exitosa
        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")
    return False

def editar_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer):
    try:
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
        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        elif response.status_code == 400:
            print(f"Error de validación: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")

def eliminar_persona(cedula):
    try:
        response = requests.delete("http://127.0.0.1:8000/personas/" + cedula)
        if response.status_code == 200:
            print("Persona eliminada con éxito.")
        elif response.status_code == 400:
            print(f"Error de validación: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")

def listar_personas():
    return