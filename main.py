from crud_alumnos import (
    insertar_alumno,
    mostrar_alumnos,
    actualizar_alumno,
    eliminar_alumno,
    truncar_tabla_alumnos
)

from crud_materias import (
    insertar_materia,
    mostrar_materias
)

from crud_inscripciones import (
    insertar_inscripcion,
    mostrar_inscripciones
)

from respaldo import respaldo_tabla
from restaurar import restaurar_tabla


while True:

    print("\n===== SISTEMA ESCUELA =====")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Agregar materia")
    print("6. Mostrar materias")
    print("7. Inscribir alumno")
    print("8. Mostrar inscripciones")
    print("9. Truncar alumnos")
    print("10. Generar respaldo")
    print("11. Restaurar tabla")
    print("12. Ver historial LOG")
    print("13. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        insertar_alumno()

    elif opcion == "2":
        mostrar_alumnos()

    elif opcion == "3":
        actualizar_alumno()

    elif opcion == "4":
        eliminar_alumno()

    elif opcion == "5":
        insertar_materia()

    elif opcion == "6":
        mostrar_materias()

    elif opcion == "7":
        insertar_inscripcion()

    elif opcion == "8":
        mostrar_inscripciones()

    elif opcion == "9":
        truncar_tabla_alumnos()

    elif opcion == "10":

        tabla = input("Tabla: ")
        respaldo_tabla(tabla)

    elif opcion == "11":

        tabla = input("Tabla: ")
        restaurar_tabla(tabla)

    elif opcion == "12":

        with open("escuela.log", "r") as archivo:
            print(archivo.read())

    elif opcion == "13":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")