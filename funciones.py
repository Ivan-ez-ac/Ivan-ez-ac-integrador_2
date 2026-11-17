"""
Biblioteca de funciones del TP Lista de Diccionarios.

Estructura de datos:
    estudiantes (list): lista donde cada elemento es un diccionario
                        que representa a un estudiante, con las claves:
        "legajo" (int): entero de cinco cifras.
        "nombre" (str): apellido y nombre.
        "genero" (str): "F", "M" o "X".
        "notas" (list): lista de cinco calificaciones enteras (1 a 10).
        "promedio" (float): promedio de las notas (None hasta que se
                            calcula en el ítem 3).
"""

LONGITUD_LEGAJO = 5
CANTIDAD_MATERIAS = 5
NOTA_MINIMA = 1
NOTA_MAXIMA = 10


# ---------------------------------------------------------------------------
# CREACIÓN DE LA ESTRUCTURA DE DATOS
# ---------------------------------------------------------------------------
def crear_estudiante() -> dict:
    """
    Crea un diccionario de estudiante con valores iniciales vacíos.

    Retorno:
        dict: estudiante con las claves legajo, nombre, genero, notas
              (lista de cinco ceros) y promedio (None).
    """
    estudiante = {
        "legajo": 0,
        "nombre": "",
        "genero": "",
        "notas": [0] * CANTIDAD_MATERIAS,
        "promedio": None
    }

    return estudiante


def crear_lista_estudiantes(cantidad: int) -> list:
    """
    Crea la lista de estudiantes: cada elemento es un diccionario
    distinto con valores iniciales vacíos.

    Argumentos:
        cantidad (int): cantidad de estudiantes.

    Retorno:
        list: lista de diccionarios.
    """
    estudiantes = [0] * cantidad

    for i in range(cantidad):
        estudiantes[i] = crear_estudiante()

    return estudiantes


def nombre_materia(indice: int) -> str:
    """
    Arma el nombre de una materia a partir del índice de su posición en
    la lista de notas. El índice 0 es MAT_1, el 1 es MAT_2, etc.

    Argumentos:
        indice (int): índice de la materia en la lista de notas.

    Retorno:
        str: nombre de la materia (por ejemplo "MAT_1").
    """
    return f"MAT_{indice + 1}"


# ---------------------------------------------------------------------------
# VALIDACIONES
# ---------------------------------------------------------------------------
def es_numero(caracter: str) -> bool:
    """
    Indica si un carácter es un dígito del 0 al 9.

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es un dígito, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if codigo >= 48 and codigo <= 57:
        retorno = True

    return retorno


def es_numerico(cadena: str) -> bool:
    """
    Indica si un texto no vacío está formado solo por dígitos.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si todos los caracteres son dígitos, False en caso
              contrario o si el texto está vacío.
    """
    retorno = cadena != ""

    for caracter in cadena:
        if es_numero(caracter) == False:
            retorno = False
            break

    return retorno


def es_letra(caracter: str) -> bool:
    """
    Indica si un carácter es una letra (mayúscula o minúscula, con o sin
    tilde, incluyendo la ñ y la ü).

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es una letra, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if (codigo >= 65 and codigo <= 90) or \
        (codigo >= 97 and codigo <= 122) or \
        codigo == 193 or codigo == 201 or codigo == 205 or \
        codigo == 211 or codigo == 218 or codigo == 220 or \
        codigo == 225 or codigo == 233 or codigo == 237 or \
        codigo == 243 or codigo == 250 or codigo == 252 or \
        codigo == 209 or codigo == 241:
        retorno = True

    return retorno


def es_alfabetico(cadena: str) -> bool:
    """
    Indica si un texto está formado solo por letras y espacios, y tiene
    al menos una letra.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = True
    hay_letra = False

    for caracter in cadena:
        if es_letra(caracter):
            hay_letra = True
        elif ord(caracter) != 32:
            retorno = False
            break

    if hay_letra == False:
        retorno = False

    return retorno


def es_genero(genero: str) -> bool:
    """
    Indica si un texto es un género válido: F, M o X (mayúscula o
    minúscula).

    Argumentos:
        genero (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if genero == "F" or genero == "M" or genero == "X" or \
        genero == "f" or genero == "m" or genero == "x":
        retorno = True

    return retorno


def es_legajo(legajo: str) -> bool:
    """
    Indica si un texto es un legajo válido: un entero de cinco cifras
    (entre 10000 y 99999, sin cero a la izquierda).

    Argumentos:
        legajo (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(legajo) and len(legajo) == LONGITUD_LEGAJO \
        and legajo[0] != "0":
        retorno = True

    return retorno


def es_nota(nota: str) -> bool:
    """
    Indica si un texto es una calificación válida: un entero entre 1 y 10.

    Argumentos:
        nota (str): texto a evaluar.

    Retorno:
        bool: True si es válida, False en caso contrario.
    """
    retorno = False

    if es_numerico(nota):
        valor = int(nota)
        if valor >= NOTA_MINIMA and valor <= NOTA_MAXIMA:
            retorno = True

    return retorno


def es_materia(materia: str, cantidad_materias: int) -> bool:
    """
    Indica si un texto es un número de materia válido: un entero entre
    1 y la cantidad de materias (índice de la materia más uno).

    Argumentos:
        materia (str): texto a evaluar.
        cantidad_materias (int): cantidad de materias.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(materia):
        valor = int(materia)
        if valor >= 1 and valor <= cantidad_materias:
            retorno = True

    return retorno


# ---------------------------------------------------------------------------
# CARGA DE DATOS (ítem 1)
# ---------------------------------------------------------------------------
def cargar_legajo() -> int:
    """
    Pide un legajo por consola y lo valida hasta que sea un entero de
    cinco cifras.

    Retorno:
        int: legajo ingresado.
    """
    legajo = input("Ingrese el legajo (5 cifras): ")

    while es_legajo(legajo) == False:
        print("Error. El legajo debe ser un número entero de 5 cifras.")
        legajo = input("Ingrese el legajo (5 cifras): ")

    return int(legajo)


def cargar_nombre() -> str:
    """
    Pide el nombre por consola y lo valida hasta que contenga solo
    letras y espacios.

    Retorno:
        str: nombre ingresado.
    """
    nombre = input("Ingrese el nombre: ")

    while es_alfabetico(nombre) == False:
        print("Error. Ingrese solamente letras y espacios.")
        nombre = input("Ingrese el nombre: ")

    return nombre


def cargar_genero() -> str:
    """
    Pide el género por consola y lo valida hasta que sea F, M o X.
    Si se ingresa en minúscula, lo devuelve en mayúscula.

    Retorno:
        str: género ("F", "M" o "X").
    """
    genero = input("Ingrese el género (F/M/X): ")

    while es_genero(genero) == False:
        print("Error. Ingrese F, M o X.")
        genero = input("Ingrese el género (F/M/X): ")

    if genero == "f":
        genero = "F"
    elif genero == "m":
        genero = "M"
    elif genero == "x":
        genero = "X"

    return genero


def cargar_nota(indice_materia: int) -> int:
    """
    Pide la calificación de una materia por consola y la valida hasta
    que sea un entero entre 1 y 10.

    Argumentos:
        indice_materia (int): índice de la materia en la lista de notas.
                              Se usa solo para armar el mensaje.

    Retorno:
        int: calificación ingresada.
    """
    mensaje = f"Ingrese la nota de {nombre_materia(indice_materia)} (1-10): "
    nota = input(mensaje)

    while es_nota(nota) == False:
        print("Error. Ingrese un entero entre 1 y 10.")
        nota = input(mensaje)

    return int(nota)


def cargar_estudiantes(estudiantes: list) -> None:
    """
    Carga los datos de todos los estudiantes en la lista de
    diccionarios. La cantidad de estudiantes es el tamaño de la lista.
    El promedio queda en None hasta que se calcula (ítem 3).

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None: modifica los diccionarios de la lista original.
    """
    for i in range(len(estudiantes)):
        print(f"\nEstudiante {i + 1}")

        estudiantes[i]["legajo"] = cargar_legajo()
        estudiantes[i]["nombre"] = cargar_nombre()
        estudiantes[i]["genero"] = cargar_genero()

        for j in range(len(estudiantes[i]["notas"])):
            estudiantes[i]["notas"][j] = cargar_nota(j)

        estudiantes[i]["promedio"] = None

    print("\nDatos cargados correctamente.")


# ---------------------------------------------------------------------------
# MOSTRAR ESTUDIANTES (ítems 2, 4 y 6)
# ---------------------------------------------------------------------------
def mostrar_estudiante(estudiante: dict) -> None:
    """
    Muestra en una fila los datos de UN estudiante: legajo, nombre,
    género, cada nota y promedio, con un separador entre valores. Si
    el promedio todavía no se calculó, muestra un guion.

    Argumentos:
        estudiante (dict): diccionario del estudiante a mostrar.

    Retorno:
        None.
    """
    fila = f"{estudiante['legajo']:<6} | {estudiante['nombre']:<26} "
    fila += f"| {estudiante['genero']:<6}"

    for j in range(len(estudiante["notas"])):
        fila += f" | {estudiante['notas'][j]:<2}"

    if estudiante["promedio"] is None:
        fila += f" | {'-':<5}"
    else:
        fila += f" | {estudiante['promedio']:<5.2f}"

    print(fila)


def mostrar_estudiantes(estudiantes: list,
                        criterio: str = "TODOS",
                        valor: int = None) -> None:
    """
    Recorre la lista de estudiantes y muestra, llamando a
    mostrar_estudiante, los que cumplan el criterio. Antes muestra un
    encabezado con las claves: LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 |
    N4 | N5 | PROM.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        criterio (str): "TODOS" muestra a todos; "LEGAJO" muestra solo
                        al estudiante cuyo legajo es igual a valor.
        valor (int): legajo buscado cuando el criterio es "LEGAJO".

    Retorno:
        None.
    """
    if criterio == "LEGAJO":
        print("\n--- ESTUDIANTE ENCONTRADO ---")
    else:
        print("\n--- INFORME DE ESTUDIANTES ---")

    titulos = f"{'LEGAJO':<6} | {'NOMBRE':<26} | {'GENERO':<6}"

    for j in range(len(estudiantes[0]["notas"])):
        titulos += f" | N{j + 1}"

    titulos += f" | {'PROM':<5}"

    print(titulos)
    print("-" * len(titulos))

    for i in range(len(estudiantes)):
        if criterio == "TODOS" or \
            (criterio == "LEGAJO" and estudiantes[i]["legajo"] == valor):
            mostrar_estudiante(estudiantes[i])


# ---------------------------------------------------------------------------
# PROMEDIOS DE LOS ESTUDIANTES (ítem 3)
# ---------------------------------------------------------------------------
def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de calificaciones, con dos
    decimales.

    Argumentos:
        notas (list): calificaciones de un estudiante.

    Retorno:
        float: promedio redondeado a 2 decimales.
    """
    suma = 0

    for i in range(len(notas)):
        suma += notas[i]

    return round(suma / len(notas), 2)


def calcular_promedios(estudiantes: list) -> None:
    """
    Calcula el promedio de cada estudiante y lo guarda en la clave
    "promedio" de su diccionario.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None: modifica los diccionarios de la lista original.
    """
    for i in range(len(estudiantes)):
        estudiantes[i]["promedio"] = calcular_promedio(estudiantes[i]["notas"])


def mostrar_promedios(estudiantes: list) -> None:
    """
    Muestra una tabla con el nombre de cada estudiante y su promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    titulos = f"{'NOMBRE':<26} | {'PROM':<5}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]['nombre']:<26} | {estudiantes[i]['promedio']:<5.2f}")


# ---------------------------------------------------------------------------
# ORDENAMIENTO (ítem 4)
# ---------------------------------------------------------------------------
def intercambiar(lista: list, i: int, j: int) -> None:
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Argumentos:
        lista (list): lista a modificar (puede contener diccionarios).
        i (int): primera posición.
        j (int): segunda posición.

    Retorno:
        None: modifica la lista original.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_por_promedio(estudiantes: list, orden: str) -> None:
    """
    Ordena la lista de estudiantes por la clave "promedio". Como cada
    elemento es un diccionario completo, un solo intercambio mueve
    todos los datos del estudiante juntos.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).
        orden (str): "ASC" (menor a mayor) o "DESC" (mayor a menor).

    Retorno:
        None: modifica la lista original.
    """
    if orden != "ASC" and orden != "DESC":
        print('Error. El orden debe ser "ASC" o "DESC".')
    else:
        n = len(estudiantes)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (orden == "DESC" and
                    estudiantes[j]["promedio"] > estudiantes[i]["promedio"]) or \
                    (orden == "ASC" and
                     estudiantes[j]["promedio"] < estudiantes[i]["promedio"]):
                    intercambiar(estudiantes, i, j)


# ---------------------------------------------------------------------------
# MATERIAS CON MAYOR PROMEDIO GENERAL (ítem 5)
# ---------------------------------------------------------------------------
def calcular_promedio_materia(estudiantes: list, indice: int) -> float:
    """
    Calcula el promedio general de una materia (la nota de esa posición
    en todos los estudiantes), con dos decimales.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        indice (int): índice de la materia en la lista de notas.

    Retorno:
        float: promedio de la materia redondeado a 2 decimales.
    """
    suma = 0

    for i in range(len(estudiantes)):
        suma += estudiantes[i]["notas"][indice]

    return round(suma / len(estudiantes), 2)


def calcular_promedios_materias(estudiantes: list) -> list:
    """
    Calcula el promedio general de cada materia. La posición de la
    lista es el índice de la materia.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        list: promedios generales de las materias.
    """
    cantidad = len(estudiantes[0]["notas"])
    promedios_materias = [0.0] * cantidad

    for j in range(cantidad):
        promedios_materias[j] = calcular_promedio_materia(estudiantes, j)

    return promedios_materias


def buscar_mayor(valores: list) -> float:
    """
    Busca el mayor valor de una lista.

    Argumentos:
        valores (list): lista de números (no vacía).

    Retorno:
        float: el mayor valor de la lista.
    """
    mayor = valores[0]

    for i in range(len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]

    return mayor


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Muestra en una fila UNA materia con su promedio general.

    Argumentos:
        indice (int): índice de la materia en la lista de notas.
        promedio (float): promedio general de la materia.

    Retorno:
        None.
    """
    print(f"{nombre_materia(indice):<10}{promedio:<10.2f}")


def mostrar_materias(promedios_materias: list,
                    criterio: str = "TODAS",
                    valor: float = None) -> None:
    """
    Recorre todas las materias y muestra, llamando a mostrar_materia,
    las que cumplan el criterio.

    Argumentos:
        promedios_materias (list): promedios generales de las materias.
        criterio (str): "TODAS" muestra todas; "MAYOR" muestra solo las
                        materias cuyo promedio es igual a valor.
        valor (float): promedio buscado cuando el criterio es "MAYOR".

    Retorno:
        None.
    """
    if criterio == "MAYOR":
        print("\n--- MATERIA/S CON MAYOR PROMEDIO GENERAL ---")
    else:
        print("\n--- PROMEDIO GENERAL DE LAS MATERIAS ---")

    titulos = f"{'MATERIA':<10}{'PROMEDIO':<10}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(promedios_materias)):
        if criterio == "TODAS" or \
            (criterio == "MAYOR" and promedios_materias[i] == valor):
            mostrar_materia(i, promedios_materias[i])


# ---------------------------------------------------------------------------
# BÚSQUEDA POR LEGAJO (ítem 6)
# ---------------------------------------------------------------------------
def buscar_indice_legajo(estudiantes: list, legajo_buscar: int) -> int:
    """
    Busca un legajo en la lista de estudiantes.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        legajo_buscar (int): legajo a buscar.

    Retorno:
        int: posición del estudiante en la lista, o -1 si no existe.
    """
    indice = -1

    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo_buscar:
            indice = i
            break

    return indice


def buscar_estudiante(estudiantes: list, legajo_buscar: int) -> None:
    """
    Busca un estudiante por legajo y, si existe, muestra todos sus
    datos (incluyendo el promedio).

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        legajo_buscar (int): legajo a buscar.

    Retorno:
        None.
    """
    indice = buscar_indice_legajo(estudiantes, legajo_buscar)

    if indice == -1:
        print("No se encontró un estudiante con ese legajo.")
    else:
        mostrar_estudiantes(estudiantes, "LEGAJO", legajo_buscar)


# ---------------------------------------------------------------------------
# REPETICIÓN DE CALIFICACIONES EN UNA MATERIA (ítem 7)
# ---------------------------------------------------------------------------
def cargar_materia(cantidad_materias: int) -> int:
    """
    Pide por consola el número de una materia (índice más uno) y lo
    valida hasta que exista.

    Argumentos:
        cantidad_materias (int): cantidad de materias.

    Retorno:
        int: número de materia ingresado (entre 1 y cantidad_materias).
    """
    mensaje = f"Ingrese el número de materia (1-{cantidad_materias}): "
    materia = input(mensaje)

    while es_materia(materia, cantidad_materias) == False:
        print(f"Error. Ingrese un número entre 1 y {cantidad_materias}.")
        materia = input(mensaje)

    return int(materia)


def contar_calificaciones(estudiantes: list, materia: int) -> list:
    """
    Cuenta cuántas veces se repite cada calificación en una materia.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        materia (int): número de materia (índice más uno).

    Retorno:
        list: lista de 10 elementos. En el índice 0 está la cantidad de
              veces que se repite la nota 1, en el índice 1 la nota 2,
              y así hasta el índice 9, que corresponde a la nota 10.
    """
    cantidades = [0] * NOTA_MAXIMA
    indice = materia - 1

    for i in range(len(estudiantes)):
        nota = estudiantes[i]["notas"][indice]
        cantidades[nota - 1] += 1

    return cantidades


def mostrar_repeticiones(cantidades: list, materia: int) -> None:
    """
    Muestra cuántas veces se repite cada calificación en una materia.

    Argumentos:
        cantidades (list): lista devuelta por contar_calificaciones.
        materia (int): número de materia (índice más uno).

    Retorno:
        None.
    """
    print(f"\n--- REPETICIÓN DE CALIFICACIONES EN {nombre_materia(materia - 1)} ---")

    for i in range(len(cantidades)):
        print(f"Nota {i + 1}: {cantidades[i]}")


# ---------------------------------------------------------------------------
# MENÚ
# ---------------------------------------------------------------------------
def mostrar_menu() -> None:
    """
    Muestra por consola las opciones del menú principal.
    """
    print("\n--- MENU DE ESTUDIANTES ---")
    print("1. Cargar datos")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedios")
    print("4. Mostrar estudiantes ordenados por promedio")
    print("5. Mostrar materia/s con mayor promedio general")
    print("6. Buscar estudiante por legajo")
    print("7. Repetición de calificaciones en una materia")
    print("8. Salir")


def opcion_cargar_datos(estudiantes: list) -> None:
    """
    Ítem 1 del menú: carga y valida los datos de todos los estudiantes.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None: modifica la lista original.
    """
    cargar_estudiantes(estudiantes)


def opcion_mostrar_estudiantes(estudiantes: list) -> None:
    """
    Ítem 2 del menú: muestra el informe con todos los estudiantes.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    mostrar_estudiantes(estudiantes)


def opcion_calcular_promedios(estudiantes: list) -> None:
    """
    Ítem 3 del menú: calcula el promedio de cada estudiante, lo guarda
    en su diccionario y lo muestra.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None: modifica los diccionarios de la lista original.
    """
    calcular_promedios(estudiantes)

    print("\n--- PROMEDIOS DE LOS ESTUDIANTES ---")
    mostrar_promedios(estudiantes)


def opcion_mostrar_ordenados(estudiantes: list) -> None:
    """
    Ítem 4 del menú: pide el sentido del orden (ASC o DESC), ordena a
    los estudiantes por promedio y muestra el informe.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).

    Retorno:
        None: modifica la lista original (queda ordenada).
    """
    orden = input("Ingrese el orden (ASC o DESC): ")

    while orden != "ASC" and orden != "DESC":
        print('Error. Ingrese "ASC" o "DESC".')
        orden = input("Ingrese el orden (ASC o DESC): ")

    ordenar_por_promedio(estudiantes, orden)
    mostrar_estudiantes(estudiantes)


def opcion_mayor_promedio_materia(estudiantes: list) -> None:
    """
    Ítem 5 del menú: calcula el promedio general de cada materia y
    muestra la/s materia/s con mayor promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    promedios_materias = calcular_promedios_materias(estudiantes)
    mayor = buscar_mayor(promedios_materias)

    mostrar_materias(promedios_materias, "MAYOR", mayor)


def opcion_buscar_estudiante(estudiantes: list) -> None:
    """
    Ítem 6 del menú: pide un legajo y muestra los datos del estudiante
    junto con su promedio.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes (con
                            el promedio ya calculado).

    Retorno:
        None.
    """
    legajo_buscar = cargar_legajo()

    buscar_estudiante(estudiantes, legajo_buscar)


def opcion_contar_calificaciones(estudiantes: list) -> None:
    """
    Ítem 7 del menú: pide el número de una materia y muestra cuántas
    veces se repite cada calificación en ella.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.

    Retorno:
        None.
    """
    materia = cargar_materia(len(estudiantes[0]["notas"]))
    cantidades = contar_calificaciones(estudiantes, materia)

    mostrar_repeticiones(cantidades, materia)


def opcion_salir() -> None:
    """
    Ítem 8 del menú: informa que el programa finaliza.
    """
    print("Saliendo del programa...")


def menu(estudiantes: list, datos_cargados: bool = False) -> None:
    """
    Controla el flujo del programa: muestra el menú, valida que se
    hayan cargado los datos (y calculado los promedios cuando
    corresponde) y llama a la función de cada ítem.

    Argumentos:
        estudiantes (list): lista de diccionarios de estudiantes.
        datos_cargados (bool): True si la lista ya viene con datos (por
                               ejemplo, datos hardcodeados para
                               pruebas). Por defecto es False.

    Retorno:
        None.
    """
    opcion = ""
    promedios_calculados = False

    while opcion != "8":
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion in ["2", "3", "4", "5", "6", "7"] and datos_cargados == False:
            print("Primero debe cargar los datos.")

        elif opcion in ["4", "6"] and promedios_calculados == False:
            print("Primero debe calcular los promedios.")

        else:
            match opcion:

                case "1":
                    opcion_cargar_datos(estudiantes)
                    datos_cargados = True
                    # Los datos cambiaron: los promedios anteriores ya no sirven
                    promedios_calculados = False

                case "2":
                    opcion_mostrar_estudiantes(estudiantes)

                case "3":
                    opcion_calcular_promedios(estudiantes)
                    promedios_calculados = True

                case "4":
                    opcion_mostrar_ordenados(estudiantes)

                case "5":
                    opcion_mayor_promedio_materia(estudiantes)

                case "6":
                    opcion_buscar_estudiante(estudiantes)

                case "7":
                    opcion_contar_calificaciones(estudiantes)

                case "8":
                    opcion_salir()

                case _:
                    print("Opcion invalida.")
