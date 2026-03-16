def validar_cedula(cedula):
    if cedula.isdigit() and len(cedula) >= 8 and len(cedula) <= 10:
        return True
    return False


def validar_email(email):
    if "@" in email and ".com" in email:
        return True
    return False


def validar_calificaciones(calificaciones):
    for c in calificaciones:
        if c < 0 or c > 5:
            return False
    return True


def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, 2)


def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


def crear_estudiante(cedula, nombre, email, calificaciones):

    if not validar_cedula(cedula):
        return None

    if not validar_email(email):
        return None

    if not validar_calificaciones(calificaciones):
        return None

    promedio = calcular_promedio(calificaciones)

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

    return estudiante


def listar_estudiantes(lista_estudiantes):

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes.")
        return

    print("Cedula | Nombre | Promedio | Desempeño")

    for e in lista_estudiantes:
        desempeño = clasificar_desempeño(e["promedio"])
        print(e["cedula"], "|", e["nombre"], "|", e["promedio"], "|", desempeño)


def buscar_estudiante(lista_estudiantes, cedula):

    for e in lista_estudiantes:
        if e["cedula"] == cedula:
            desempeño = clasificar_desempeño(e["promedio"])
            print(e["nombre"], "| Promedio:", e["promedio"], "| Desempeño:", desempeño)
            return

    print("Estudiante no encontrado")


def main():

    estudiantes = []

    while True:

        print("\n1. Agregar estudiante")
        print("2. Ver lista")
        print("3. Buscar por cedula")
        print("4. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":

            cedula = input("Cedula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            datos = input("Calificaciones separadas por coma: ")
            partes = datos.split(",")

            calificaciones = []
            for p in partes:
                calificaciones.append(float(p))

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante == None:
                print("Datos invalidos")
            else:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print("Estudiante agregado. Promedio:", estudiante["promedio"], "|", desempeño)

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":
            cedula = input("Cedula a buscar: ")
            buscar_estudiante(estudiantes, cedula)

        elif opcion == "4":
            print("Fin del programa")
            break

        else:
            print("Opcion invalida")


main()