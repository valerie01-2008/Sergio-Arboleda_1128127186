import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

def calcular_potencia(base, exponente):
    return math.pow(base, exponente)

def main():
    while True:
        print("\n--- CALCULADORA CIENTÍFICA ---")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            radio = float(input("Ingresa el radio: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es {area:.2f}")

        elif opcion == "2":
            a = float(input("Ingresa el primer cateto: "))
            b = float(input("Ingresa el segundo cateto: "))
            h = calcular_hipotenusa(a, b)
            print(f"La hipotenusa es {h:.2f}")

        elif opcion == "3":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = calcular_potencia(base, exponente)
            print(f"El resultado es {resultado:.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")

main()