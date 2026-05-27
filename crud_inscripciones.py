from conexion import obtener_conexion
from historial import registrar_log


def insertar_inscripcion():

    id_alumno = input("ID Alumno: ")
    id_materia = input("ID Materia: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO inscripciones(id_alumno, id_materia)
    VALUES(%s, %s)
    """

    cursor.execute(sql, (id_alumno, id_materia))

    conexion.commit()

    print("Inscripción realizada")

    registrar_log(
        f"Inscripción alumno {id_alumno} materia {id_materia}"
    )

    conexion.close()


def mostrar_inscripciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
    SELECT inscripciones.id,
           alumnos.nombre,
           materias.nombre
    FROM inscripciones
    INNER JOIN alumnos
    ON inscripciones.id_alumno = alumnos.id
    INNER JOIN materias
    ON inscripciones.id_materia = materias.id
    """

    cursor.execute(sql)

    datos = cursor.fetchall()

    for fila in datos:
        print(fila)

    conexion.close()