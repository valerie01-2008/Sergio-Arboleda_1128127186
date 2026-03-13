# Inicializar variables
contador = 0
suma = 0
mayor = None
menor = None
pares = 0
impares = 0

while True:
    numero = input("Ingresa un número (0 para terminar): ")
    
    # Validar que sea un número
    if not numero.lstrip('-').isdigit():  # permite negativos
        print("Por favor ingresa un número válido.")
        continue
    
    numero = int(numero)
    
    # Condición de salida
    if numero == 0:
        break
    
    # Actualizar contador y suma
    contador += 1
    suma += numero
    
    # Actualizar mayor y menor
    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero
    
    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
if contador == 0:
    print("No se ingresaron números.")
else:
    promedio = suma / contador
    print("\n--- Estadísticas ---")
    print(f"Cantidad total de números: {contador}")
    print(f"Suma de todos los números: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")