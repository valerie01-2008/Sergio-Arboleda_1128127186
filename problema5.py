cantidad = 0
suma = 0
pares = 0
impares = 0
mayor = None
menor = None

numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:

    cantidad = cantidad + 1
    suma = suma + numero

    if mayor is None or numero > mayor:
        mayor = numero

    if menor is None or numero < menor:
        menor = numero

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    numero = int(input("Ingrese otro número (0 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("Cantidad de números:", cantidad)
    print("Suma:", suma)
    print("Promedio:", promedio)
    print("Mayor:", mayor)
    print("Menor:", menor)
    print("Pares:", pares)
    print("Impares:", impares)
else:
    print("No se ingresaron números")