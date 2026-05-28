import json
from conexion import obtener_conexion


def restaurar_tabla(nombre_tabla):

    archivo_ruta = f"respaldos/{nombre_tabla}.json"

    try:
        with open(archivo_ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except FileNotFoundError:
        print(f"No existe el respaldo de la tabla: {nombre_tabla}")
        return

    if len(datos) == 0:
        print("El archivo de respaldo está vacío")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

    cursor.execute(f"TRUNCATE TABLE {nombre_tabla}")

    
    for fila in datos:

        columnas = ", ".join(fila.keys())
        valores = ", ".join(["%s"] * len(fila))

        sql = f"""
        INSERT INTO {nombre_tabla} ({columnas})
        VALUES ({valores})
        """

        cursor.execute(sql, tuple(fila.values()))

    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    conexion.commit()
    conexion.close()

    print(f"Tabla '{nombre_tabla}' restaurada correctamente desde JSON")