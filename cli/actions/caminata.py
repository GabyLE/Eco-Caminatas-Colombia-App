import requests

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

def editar_caminata():
    return

def eliminar_caminata():
    return

def listar_caminatas():
    return