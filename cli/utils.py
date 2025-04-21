import re
from tabulate import tabulate

def validar_cedula(cedula):
    # Verifica que la cédula solo tenga números y tenga una longitud específica
    if re.match(r'^\d+$', cedula) and len(cedula) >= 6 and len(cedula) <= 10:  # Ajusta la longitud según el caso
        return True
    else:
        print("Cédula inválida. Debe ser un número con entre 6 y 10 dígitos.")
        return False

def validar_nombre(nombre):
    if len(nombre.strip()) > 0:  # Verifica que no esté vacío
        return True
    else:
        print("El nombre no puede estar vacío.")
        return False
    
def solicitar_datos_persona(metodo="crear"):
    if metodo == "crear":
        nombre = input("Ingrese el nombre de la persona: ")
        cedula = input(f"Ingrese la cédula de {nombre}: ")
        celular = input(f"Ingrese el celular de {nombre}: ")
        correo = input(f"Ingrese el correo electrónico de {nombre}: ")
        nombre_contemer = input(f"Ingrese el nombre del contacto de emergencia de {nombre}: ")
        celular_contemer = input(f"Ingrese el celular del contacto de emergencia de {nombre}: ")
        
        print(f"Los datos están correctos?" 
        f"\n Nombre: {nombre}" 
        f"\n Cédula: {cedula}" 
        f"\n Celular: {celular}" 
        f"\n Correo: {correo}" 
        f"\n Nombre contacto de emergencia: {nombre_contemer}" 
        f"\n Celular contacto de emergencia: {celular_contemer}")

        return (nombre, cedula, celular, correo, nombre_contemer, celular_contemer)
    
    elif metodo == "actualizar":
        nombre = input("Ingrese el nombre de la persona: ")
        celular = input(f"Ingrese el celular de {nombre}: ")
        correo = input(f"Ingrese el correo electrónico de {nombre}: ")
        nombre_contemer = input(f"Ingrese el nombre del contacto de emergencia de {nombre}: ")
        celular_contemer = input(f"Ingrese el celular del contacto de emergencia de {nombre}: ")
        
        print(f"Los datos están correctos?" 
        f"\n Nombre: {nombre}" 
        f"\n Celular: {celular}" 
        f"\n Correo: {correo}" 
        f"\n Nombre contacto de emergencia: {nombre_contemer}" 
        f"\n Celular contacto de emergencia: {celular_contemer}")

        return (nombre, celular, correo, nombre_contemer, celular_contemer)

def solicitar_datos_caminata():
    nombre = input("Ingrese el nombre de la caminata: ")
    kilometros = input(f"Ingrese los kilómetros de la ruta {nombre}: ")
    duracion = input(f"Ingrese la duración de la ruta {nombre}: ")
    
    print(f"Los datos están correctos?" 
      f"\n Nombre: {nombre}" 
      f"\n Kilómetros: {kilometros}" 
      f"\n Duración: {duracion}")

    return (nombre, kilometros, duracion)


def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Senderista")
    print("2. Caminata")
    print("3. Registro")
    print("4. Salir")

def imprimir_personas_tabla(datos):
    personas = datos.get("personas", [])
    if not personas:
        print("No hay personas registradas.")
        return

    tabla = []
    for p in personas:
        tabla.append([
            p["_id"],
            p["nombre_completo"],
            p["celular"],
            p["correo"],
            p["contacto_emergencia"]["nombre"],
            p["contacto_emergencia"]["celular"],
            len(p["caminatas_asistidads"])
        ])

    headers = ["Cédula", "Nombre", "Celular", "Correo", "Contacto Emergencia", "Celular CE", "# Caminatas"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def imprimir_caminatas_tabla(datos):
    caminatas = datos.get("caminatas", [])
    if not caminatas:
        print("No hay caminatas registradas.")
        return

    tabla = []
    for c in caminatas:
        tabla.append([
            c["nombre"],
            c["kilometros"],
            c["duracion"]
        ])

    headers = ["Nombre", "Km", "Duración"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))