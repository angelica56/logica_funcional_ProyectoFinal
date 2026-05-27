from conexion import obtener_conexion
from historial import registrar_log


def insertar_alumno():

    nombre = input("Nombre: ")

    if nombre.strip() == "":
        print("Nombre inválido")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO alumnos(nombre) VALUES(%s)"

    cursor.execute(sql, (nombre,))

    conexion.commit()

    print("Alumno agregado")

    registrar_log(f"Alumno agregado: {nombre}")

    conexion.close()


def mostrar_alumnos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM alumnos")

    datos = cursor.fetchall()

    if len(datos) == 0:
        print("No hay alumnos registrados")

    else:
        for fila in datos:
            print(fila)

    conexion.close()


def actualizar_alumno():

    id_alumno = input("ID alumno: ")
    nuevo_nombre = input("Nuevo nombre: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "UPDATE alumnos SET nombre=%s WHERE id=%s"

    cursor.execute(sql, (nuevo_nombre, id_alumno))

    conexion.commit()

    print("Alumno actualizado")

    registrar_log(f"Alumno actualizado ID {id_alumno}")

    conexion.close()


def eliminar_alumno():

    id_alumno = input("ID alumno: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "DELETE FROM alumnos WHERE id=%s"

    cursor.execute(sql, (id_alumno,))

    conexion.commit()

    print("Alumno eliminado")

    registrar_log(f"Alumno eliminado ID {id_alumno}")

    conexion.close()


def truncar_tabla_alumnos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

    cursor.execute("TRUNCATE TABLE inscripciones")
    cursor.execute("TRUNCATE TABLE alumnos")

    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    conexion.commit()

    print("Tabla alumnos vaciada")

    registrar_log("Tabla alumnos truncada")

    conexion.close()