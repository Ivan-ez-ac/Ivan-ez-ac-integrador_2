from funciones import *

# Datos hardcodeados SOLO PARA PRUEBAS (Nota 0 del TP).
# La lista ya viene cargada, por eso se pasa datos_cargados=True.
estudiantes = [
    {"legajo": 20415, "nombre": "Perez Ana", "genero": "F",
    "notas": [8, 9, 7, 10, 6], "promedio": None},
    {"legajo": 20301, "nombre": "Gomez Luis", "genero": "M",
    "notas": [6, 7, 5, 8, 9], "promedio": None},
    {"legajo": 20387, "nombre": "Diaz Sol", "genero": "X",
    "notas": [10, 10, 10, 10, 10], "promedio": None},
    {"legajo": 20122, "nombre": "Ruiz Marta", "genero": "F",
    "notas": [5, 4, 6, 7, 3], "promedio": None},
    {"legajo": 20560, "nombre": "Lopez Juan", "genero": "M",
    "notas": [10, 8, 9, 10, 9], "promedio": None},
    {"legajo": 20244, "nombre": "Mena Lucia", "genero": "F",
    "notas": [7, 7, 8, 9, 6], "promedio": None}
]

menu(estudiantes, True)
