from conexion import obtener_conexion
from historial import registrar_log


def insertar_materia():

    nombre = input("Nombre materia: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO materias(nombre) VALUES(%s)"

    cursor.execute(sql, (nombre,))

    conexion.commit()

    print("Materia agregada")

    registrar_log(f"Materia agregada: {nombre}")

    conexion.close()


def mostrar_materias():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM materias")

    datos = cursor.fetchall()

    for fila in datos:
        print(fila)

    conexion.close()