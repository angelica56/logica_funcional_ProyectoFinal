import json
from conexion import obtener_conexion


def respaldo_tabla(nombre_tabla):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM {nombre_tabla}")

    datos = cursor.fetchall()

    columnas = [col[0] for col in cursor.description]

    resultado = []

    for fila in datos:
        resultado.append(dict(zip(columnas, fila)))

    with open(f"respaldos/{nombre_tabla}.json", "w", encoding="utf-8") as archivo:
        json.dump(resultado, archivo, indent=4, ensure_ascii=False)

    print(f"Respaldo de {nombre_tabla} generado")

    conexion.close()