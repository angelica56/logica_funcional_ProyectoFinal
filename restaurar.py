import json
from conexion import obtener_conexion


def restaurar_tabla(nombre_tabla):

    with open(f"respaldos/{nombre_tabla}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(f"TRUNCATE TABLE {nombre_tabla}")

    for fila in datos:

        columnas = ", ".join(fila.keys())
        placeholders = ", ".join(["%s"] * len(fila))

        sql = f"""
        INSERT INTO {nombre_tabla}
        ({columnas})
        VALUES ({placeholders})
        """

        cursor.execute(sql, tuple(fila.values()))

    conexion.commit()

    print(f"Tabla {nombre_tabla} restaurada")

    conexion.close()