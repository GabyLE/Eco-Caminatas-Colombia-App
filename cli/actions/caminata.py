import requests
from utils import imprimir_caminatas_tabla

def añadir_caminata(nombre, kilometros, duracion):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/caminatas", 
            json={
                "nombre": nombre,
                "kilometros": kilometros,
                "duracion": duracion
            }
        )

        if response.status_code == 200:
            print("Caminata añadida con éxito.")
        elif response.status_code == 400:
            print(f"No se pudo añadir la caminata: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")

def buscar_caminata(nombre):
    try:
        response = requests.get("http://127.0.0.1:8000/caminatas/buscar/?nombre=" + nombre)
        if response.status_code == 200:
            datos = response.json()
            imprimir_caminatas_tabla(datos)

        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")
    return

def obtener_caminata(nombre):
    try:
        response = requests.get("http://127.0.0.1:8000/caminatas/" + nombre)

        if response.status_code == 200:
            datos = response.json()
            print("Datos actuales:")
            print("Nombre: ", datos["nombre"])
            print("Kilómetros:", datos["kilometros"])
            print("Duración: ", datos["duracion"])
            return True  # Indicador de que fue exitosa
        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")
    return False

def editar_caminata(nombre,nombre_nuevo, kilometros, duracion):
    try:
        response = requests.put("http://127.0.0.1:8000/caminatas/" + nombre, 
                                json={
                                    "nombre": nombre_nuevo,
                                    "kilometros": kilometros,
                                    "duracion": duracion
                                })
        if response.status_code == 200:
            print("Caminata actualizada con éxito.")
        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        elif response.status_code == 400:
            print(f"Error de validación: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")

def eliminar_caminata(nombre):
    try:
        response = requests.delete("http://127.0.0.1:8000/caminatas/" + nombre)
        if response.status_code == 200:
            print("Caminata eliminada con éxito.")
        elif response.status_code == 400:
            print(f"Error de validación: {response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")

def listar_caminatas():
    try:
        response = requests.get("http://127.0.0.1:8000/caminatas")
        if response.status_code == 200:
            datos = response.json()
            imprimir_caminatas_tabla(datos)

        elif response.status_code == 404:
            print(f"{response.json().get('detail')}")
        else:
            print(f"Error inesperado ({response.status_code}): {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con el servidor: {e}")