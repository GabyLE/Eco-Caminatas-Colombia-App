import sys
from actions.persona import añadir_persona, editar_persona, eliminar_persona, listar_personas
#from actions.caminata import añadir_caminata, editar_caminata, eliminar_caminata, ver_caminata
#from actions.registro import añadir_registro, editar_registro, eliminar_registro, ver_registro

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Senderista")
    print("2. Caminata")
    print("3. Registro")
    print("4. Salir")

def acciones_persona():
    while True:
        print("Acciones disponibles para Senderista:")
        print("1. Añadir Senderista")
        print("2. Editar Senderista")
        print("3. Eliminar Senderista")
        print("4. Ver listado de Senderistas")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
        # Llamar a la función para añadir persona
            nombre = input("Ingrese el nombre de la persona: ")
            cedula = input(f"Ingrese la cédula de {nombre}: ")
            celular = input(f"Ingrese el celular de {nombre}: ")
            correo = input(f"Ingrese el correo electrónico de {nombre}: ")
            nombre_contemer = input(f"Ingrese el nombre del contacto de emergencia de {nombre}: ")
            celular_contemer = input(f"Ingrese el celular del contacto de emergencia de {nombre}")
            
            añadir_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer)  # Llama a la función de añadir persona
        
        elif opcion == "2":
                editar_persona()
        elif opcion == "3":
            eliminar_persona()
        elif opcion == "4":
            listar_personas()
        elif opcion == "5":
            break  # Vuelve al menú principal
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def acciones_caminata():
    while True:
        print("Acciones disponibles para Caminata:")
        print("1. Añadir Caminata")
        print("2. Editar Caminata")
        print("3. Eliminar Caminata")
        print("4. Ver listado de Caminatas")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            añadir_caminata()
        elif opcion == "2":
            editar_caminata()
        elif opcion == "3":
            eliminar_caminata()
        elif opcion == "4":
            ver_caminata()
        elif opcion == "5":
            break  # Vuelve al menú principal
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def acciones_registro():
    while True:
        print("Acciones disponibles para Registro:")
        print("1. Añadir Registro")
        print("2. Ver Registro de un Senderista")
        print("3. Ver Registros de una Caminata")
        print("4. Ver listado de Registros")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            añadir_registro()
        elif opcion == "2":
            ver_registro()
        elif opcion == "3":
            ver_registro_caminata()
        elif opcion == "4":
            ver_registro()
        elif opcion == "5":
            break  # Vuelve al menú principal
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            acciones_persona()
        elif opcion == "2":
            acciones_caminata()
        elif opcion == "3":
            acciones_registro()
        elif opcion == "4":
            print("¡Adiós!")
            sys.exit(0)
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
