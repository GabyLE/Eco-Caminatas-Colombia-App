import re

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
    
def solicitar_datos_persona():
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


def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Senderista")
    print("2. Caminata")
    print("3. Registro")
    print("4. Salir")
