import random

# Definir los caracteres posibles
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiales = "!@#$%"

todos_caracteres = mayusculas + minusculas + numeros + especiales

while True:
    # Pedir longitud de la contraseña
    longitud = input("Ingresa la longitud de la contraseña (8-20): ")
    
    # Validar que sea un número
    if not longitud.isdigit():
        print("Por favor ingresa un número válido.")
        continue
    
    longitud = int(longitud)
    
    # Validar rango de longitud
    if longitud < 8 or longitud > 20:
        print("La longitud debe ser entre 8 y 20.")
        continue
    
    # Generar contraseña
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(todos_caracteres)
    
    print(f"Tu contraseña generada es: {contrasena}")
    
    # Preguntar si quiere generar otra
    otra = input("¿Quieres generar otra contraseña? (s/n): ").lower()
    if otra != "s":
        print("¡Hasta luego!")
        break