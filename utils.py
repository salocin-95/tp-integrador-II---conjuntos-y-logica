from datetime import datetime



# ------------------------------ 1. OPERACIONES CON DNI --------------------------------------------------------------------

# Funcion para union

def calculo_union(lista_dni):
    conjuntos_dni = [set(dni) for dni in lista_dni]         # Con set nos aseguramos de guardar elementos unicos y desordenados para evitar duplicidades de digitos
    union_dni = set.union(*conjuntos_dni)                   # Realizamos el calculo de union
    union_ordenada = sorted([int(d) for d in union_dni])    # Sorted, al igual que sort, ordena los elementos para presentarlos de forma prolija
    print(f"La union de los conjuntos es: {union_ordenada}")

# Funcion para interseccion

def calculo_interseccion(lista_dni):
    conjuntos_dni = [set(dni) for dni in lista_dni]                       # Con set nos aseguramos de guardar elementos unicos y desordenados para evitar duplicidades de digitos
    interseccion_dni = set.intersection(*conjuntos_dni)                   # Realizamos el calculo de interseccion
    interseccion_ordenada = sorted([int(d) for d in interseccion_dni])    # Sorted, al igual que sort, ordena los elementos para presentarlos de forma prolija
    print(f"La interseccion de los conjuntos es: {interseccion_ordenada}")

# Funcion para diferencia

def calculo_diferencia(lista_dni):
    conjuntos_dni = [set(dni) for dni in lista_dni]                        # Con set nos aseguramos de guardar elementos unicos y desordenados para evitar duplicidades de digitos
    diferencia_dni = set.difference(*conjuntos_dni)                        # Realizamos el calculo de diferencia 
    diferencia_ordenada = sorted([int(d) for d in diferencia_dni])         # Sorted, al igual que sort, ordena los elementos para presentarlos de forma prolija
    print(F"La diferencia de los conjuntos es: {diferencia_ordenada}")

# Funcion para diferencia simetrica

def calculo_diferencia_simetrica(lista_dni):
    conjuntos_dni = [set(dni) for dni in lista_dni]                                        # Con set nos aseguramos de guardar elementos unicos y desordenados para evitar duplicidades de digitos
    acum = conjuntos_dni[0]                                                                # Creamos una variable acumuladora con el primer conjunto 
    for i in conjuntos_dni[1:]:                                                            # Recorremos en bucle todos los conjuntos a partir del 2do elemento de la lista
        acum = acum.symmetric_difference(i)                                                # Actualizamos la variable acumuladora con la diferencia del ultimo conjunto guardado con el siguiente de la lista
    diferencia_simetrica_ordenada = sorted(list(acum))                                     # Convertimos el resultado a lista y lo ordenamos para mantener cohecion con el resto de programas y manejo de datos
    print(f"La diferencia simetrica de los conjuntos es: {diferencia_simetrica_ordenada}") 


# ------------------------------ 2. SUMA DE DIGITOS DE CADA DNI --------------------------------------------------------------------


# Funcion para suma de digitos de un DNI

def suma_digitos(lista_dni):                            # Definimos la funcion
    for x in lista_dni:                                 # Se recorre las listas
        dni_str = x                                     # Se obtiene el string de cada lista 
        digitos = [int(d) for d in dni_str]             # Se transforman los strings de las listas en enteros
        suma = sum(digitos)                             # Se suman los digitos ya cambiados a enteros
        print(f"La suma de los digitos del DNI {x} es: {suma}")    


# ------------------------------ 3. CONTADOR DE CUANTO APARECE CADA DIGITO POR DNI --------------------------------------------------------------------


# Funcion para contar cuantas veces aparece cada digito

def contador_digitos(lista_dni):
    lista_unificada = "".join(lista_dni)            # Unificamos todos los elementos de la lista para poder recorrerlos de forma conjunta
    x = 0                                           # Iniciamos una variable de incremento para el while y para que funcione de comparacion
    while x < 10:                                   # Usamos un while desde 0 a 9 para contar todos los digitos unicos
        acum = 0                                    # Iniciamos una variable que acumule la cantidad de veces que aparece el digito
        for i in lista_unificada:                   # Usamos for para recorrer la lista de digitos conjuntos
            if i == str(x):                         # Usamos un if para la comparacion, en caso de ser positiva suma el acumulador
                acum += 1
        print(f"Dígito {x}: {acum} veces")          
        x += 1                                      # Aumentamos la variable x por cada vuelta para que el while termine en 9


# ------------------------------ 4. CONDICIONES LOGICAS PARA EXPRESIONES ESCRITAS --------------------------------------------------------------------


# Funcion para ver si un digito aparece en todos los conjuntos

def digito_compartido(lista_dni):
    conjuntos_dni = [set(dni) for dni in lista_dni]  # La funcion comparte misma logica que la interseccion, solo se agrega un if para enviar diferentes mensajes.
    digito_compartido_dni = set.intersection(*conjuntos_dni)                   
    digito_compartido_ordenado = sorted([int(d) for d in digito_compartido_dni])    
    if digito_compartido_ordenado:
        print(f"Los digitos que aparecen en todos los DNI son: {digito_compartido_ordenado}")
    else:
        print("No hay digitos compartidos en todos los DNI.")

# Funcion que devuelve que DNI ingresado es par y cual impar 

def es_par_impar(lista_dni):
    digitos = [int(d) for d in lista_dni] 
    for dni in digitos:
        if dni % 2 == 0:
            print(f"El dni {dni} es par")
        else:
            print(f"El dni {dni} es impar")

# Funcion para ver si un DNI es anagrama de otro

def anagrama(lista_dni):
    encontrados = False
    for i in range(len(lista_dni) - 1):                                         # Recorremos toda la lista_dni
        dni_actual = lista_dni[i]                                               # Almacenamos el dni que estamos recorriendo en una variable para compararlo
        digitos_ordenados = sorted(dni_actual)                                  # Ordenamos el DNI que vamos a comparar
        for j in range(i + 1, len(lista_dni)):                                  # Iniciamos el bucle con el cual realizamos la comparacion
            dni_comparar = lista_dni[j]                                         # Almacenamos el DNI a comparar en esta variable
            comparar_ordenado = sorted(dni_comparar)                            # Lo ordenamos para que, en caso de ser anagrama, esten ambos iguales
            if digitos_ordenados == comparar_ordenado:                          # Comparamos las dos variables de almacenamiento
                print(f"El DNI {dni_actual} es un anagrama de {dni_comparar}")  # Devolvemos si algun DNI del conjunto es anagrama del otro
    if not encontrados:
        print("No se encontraron DNIs que sean anagramas entre sí.")
        
# =============== Expresiones lógicas ===============

# Expresión 1: combinacion amplia

def combinacion_amplia(lista_dni):
    if len(lista_dni) < 3:                                                       # Se asegura de que por lo menos hayan 3 DNIs en la lista
        print("Se necesitan al menos 3 DNIs para evaluar esta expresión.")
        return
    A = set(lista_dni[0])                                                        # Se toman los primeros 3 DNIs de la lista de DNIs
    B = set(lista_dni[1])
    C = set(lista_dni[2])
    if len(A) > len(B) and any(int(d) % 2 != 0 for d in C):                      # La primera parte evalua si el conjunto A tiene mas dígitos unicos que el conjunto B
        print(" Se cumple la condición de combinación amplia")                   # La segunda parte combierte todos los caracteres del conjunto c en enteros y verifica si son pares
    else:
        print(" No se cumple la condición de combinación amplia")

# Expresión 2: grupo sin ceros

def grupo_sin_ceros(lista_dni):
    conjuntos = [set(dni) for dni in lista_dni]                                  # Convierte los DNIs en conjuntos
    sin_ceros = True                                                             # Se abre una variable con valor True para mas adelante
    for c in conjuntos:                                                          # Analiza cada DNI de la variable "Conjuntos"
        if "0" in c:                                                             # Busca el 0 en cada conjunto
            sin_ceros = False                                                    # Si se encuentra un 0 dentro del conjunto entonces la condicion es falsa y se detiene el bucle
            break                                                                
    if sin_ceros:
        print(" Grupo sin ceros")
    else:
        print(" Hay al menos un conjunto con ceros")
        
# Menu principal

def menu_principal(lista_dni):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Calcular Unión de dígitos")
        print("2. Calcular Intersección de dígitos")
        print("3. Calcular Diferencia de dígitos")
        print("4. Calcular Diferencia Simétrica de dígitos")
        print("5. Sumar dígitos de cada DNI")
        print("6. Contar cuántas veces aparece cada dígito")
        print("7. Mostrar dígitos que aparecen en todos los DNIs")
        print("8. Mostrar cuáles DNIs son pares e impares")
        print("9. Encontrar DNIs que son anagramas entre sí")
        print("10. Evaluar expresiones lógicas personalizadas")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            calculo_union(lista_dni)
        elif opcion == "2":
            calculo_interseccion(lista_dni)
        elif opcion == "3":
            calculo_diferencia(lista_dni)
        elif opcion == "4":
            calculo_diferencia_simetrica(lista_dni)
        elif opcion == "5":
            suma_digitos(lista_dni)
        elif opcion == "6":
            contador_digitos(lista_dni)
        elif opcion == "7":
            digito_compartido(lista_dni)
        elif opcion == "8":
            es_par_impar(lista_dni)
        elif opcion == "9":
            anagrama(lista_dni)
        elif opcion == "10":
            while True:
                print("\n--- EXPRESIONES LÓGICAS ---")
                print("1. Expresión 1 - Condición de combinación amplia")
                print("2. Expresión 2 - Busqueda de ceros")
                print("0. Volver al menú principal")
                eleccion = input("Seleccione una opción: ")
                if eleccion == "1":
                    combinacion_amplia(lista_dni)
                elif eleccion == "2":
                    grupo_sin_ceros(lista_dni)
                elif eleccion == "0":
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
        elif opcion == "0":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")
        continuar = input("\n¿Desea realizar otra operación? (y: Sí / ENTER: No): ")
        if continuar.lower() != "y":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

# ------------------------------ 2. OPERACIONES CON FECHAS DE NACIMIENTO  --------------------------------------------------------------------

def nacimientos():
    
    este_anio = datetime.now().year

    def es_bisiesto(anio):
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    def contador():
        nacimientos = []
        edades = []
        print("Ingrese las fechas de nacimiento o ENTER para continuar.")
        while True:
            user_input = (input("Ingrese el año de nacimiento: "))
            if user_input == "":
                break
            if not user_input.isdigit():
                print("Entrada inválida. Intente nuevamente.")
                continue
            nacimientos.append(int(user_input))

        if not nacimientos:
            print("No se ingresaron años de nacimiento.")
            return

        # Si dos integrantes tienen el mismo año de nacimiento dar un dato ficticio sino aclarar que no hay fechas repetidas
        # len(set(nacimientos)) La funcion set crea un nuevo set sin repetir ningun elemento por lo que si el len de set nacimientos es menor al len nacimientos
        # quiere decir que hay un año de nacimiento repetido
        if len(set(nacimientos)) < len(nacimientos):
            print("Dato fictio")
        else:
            print("No hay fechas de nacimiento repetidas.")

        # Cuenta los años pares e impares
        impar = 0
        par = 0

        for anio in nacimientos:
            if anio%2 == 0:
                print(f"{anio} es par")
                par += 1
            else:
                print(f"{anio} es impar")
                impar += 1
        
        print(f"Las personas que nacieron en año impar: {impar}\nLos que nacieron en año par: {par}")
        
        # Calcula la generación z
        if all(anio >= 2000 for anio in nacimientos):
            print("Grupo Z")


        # Si alguno nacio en un año bisiesto
        # Si un año en la lista es bisiesto deberia devolver true y el año
        for anio in nacimientos:
            if es_bisiesto(anio):
                print(f"El año bisiesto es: {anio}")
                print("Tenemos un año especial")
                break

        for _ in nacimientos:
            edades.append(este_anio - _)


        producto_cartesiano = {(a, b) for a in set(nacimientos) for b in set(edades)}
        print(f"Producto cartesiano de {set(nacimientos)} x {set(edades)} es: {producto_cartesiano}")


        
    contador()