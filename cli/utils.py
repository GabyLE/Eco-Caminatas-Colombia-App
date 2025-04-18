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