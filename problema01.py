suma = 0
mayor = -1
menor = 6
nombre_mayor = ""
nombre_menor = ""

for i in range(5):
    nombre = input("Nombre del estudiante: ")

    edad = int(input("Edad: "))
    while edad < 5 or edad > 100:
        edad = int(input("Edad inválida. Ingrese edad entre 5 y 100: "))

    nota = float(input("Calificación (0-5): "))
    while nota < 0 or nota > 5:
        nota = float(input("Calificación inválida. Ingrese entre 0 y 5: "))

    suma = suma + nota

    if nota > mayor:
        mayor = nota
        nombre_mayor = nombre

    if nota < menor:
        menor = nota
        nombre_menor = nombre

promedio = suma / 5

print("Estudiante con mayor calificación:", nombre_mayor, mayor)
print("Estudiante con menor calificación:", nombre_menor, menor)
print("Promedio de calificaciones:", promedio)
