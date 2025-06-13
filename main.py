from utils import *

lista_dni = []

# Menu inicial de interaccion
def menu():
    while True:
        user_input = input("Elija una opción:\n1. DNI\n2. Nacimientos\nENTER para salir\n")
        if user_input == "":
            print("Gracias por utilizar el programa.")
            break
        elif user_input == "1":
            menu_dni()
        elif user_input == "2":
            nacimientos()
        else:
            print("Ingrese una opción correcta")
           
def menu_dni():
    while True:
        dni = input("Ingrese un DNI (solo numeros) o ENTER para salir: ")
        if dni == "" and len(lista_dni) >= 2:                                                 # Este if se encarga de terminar el bucle cuando se presione enter
            print("Perfecto, trabajaremos con estos datos brindados hasta ahora.")
            break               
        if dni in lista_dni:                                                        # Este if se encarga de validar si el DNI ya fue ingresado, informa y no almacena
            print("Ese DNI ya fue ingresado")
            continue
        if not dni.isdigit():                                                       # Este if se encarga de validar que el tipo de dato ingresado sea number, caso contrario informa y no almacena
            print("Por favor, ingrese solo números.")
            continue
        lista_dni.append(dni)
    # Asegura que al menos se ingresen dos conjuntos númericos para que no tiren error el resto de las funciones
    if len(lista_dni) < 2:
        print("Necesita al menos dos numeros para poder trabajar")
    if len(lista_dni) >= 2:
        menu_principal(lista_dni)

menu()