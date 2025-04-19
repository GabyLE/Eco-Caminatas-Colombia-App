import sys
from utils import solicitar_datos_persona, mostrar_menu
from actions.persona import añadir_persona, editar_persona, eliminar_persona, listar_personas, obtener_persona, buscar_persona
#from actions.caminata import añadir_caminata, editar_caminata, eliminar_caminata, ver_caminata
#from actions.registro import añadir_registro, editar_registro, eliminar_registro, ver_registro

def acciones_persona():
    while True:
        print("Acciones disponibles para Senderista:")
        print("1. Añadir Senderista")
        print("2. Editar Senderista")
        print("3. Eliminar Senderista")
        print("4. Ver listado de Senderistas")
        print("5. Buscar Senderista (por nombre)")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            
            while True:
                nombre, cedula, celular, correo, nombre_contemer, celular_contemer = solicitar_datos_persona()
                print("Los datos están correctos?")
                sel = input("1. Sí \n2. No\n")

                if sel == "1":
                    añadir_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer)  # Llama a la función de añadir persona
                    break

        elif opcion == "2":
            while True:
                cedula = input("Ingrese la cédula de la persona que va a actualizar: ")
                encontrada = obtener_persona(cedula)

                if not encontrada:
                    repetir = input("¿Deseas intentar con otra cédula? (s/n): ")
                    if repetir.lower() != "s":
                        break
                    continue

                print("¿Es la persona correcta?")
                sel = input("1. Sí \n2. No\n")

                if sel == "1":
                    while True:
                        nombre, cedula_nueva, celular, correo, nombre_contemer, celular_contemer = solicitar_datos_persona()
                        print("¿Los datos están correctos?")
                        sel = input("1. Sí \n2. No\n")

                        if sel == "1":
                            editar_persona(cedula, nombre, celular, correo, nombre_contemer, celular_contemer)
                            break
                break

        elif opcion == "3":
             while True:
                cedula = input("Ingrese la cédula de la persona que va a eliminar: ")
                encontrada = obtener_persona(cedula)

                if not encontrada:
                    repetir = input("¿Deseas intentar con otra cédula? (s/n): ")
                    if repetir.lower() != "s":
                        break
                    continue

                print("¿Es la persona correcta?")
                sel = input("1. Sí \n2. No\n")

                if sel == "1":
                    eliminar_persona(cedula)
                    break
                break
                
                
        elif opcion == "4":
            listar_personas()
        elif opcion == "5":
            buscar_persona()
        elif opcion == "6":
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
