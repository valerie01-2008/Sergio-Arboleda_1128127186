def calcular_imc(peso, altura):
    # Calcula el IMC y lo redondea a 2 decimales
    imc = peso / (altura ** 2)
    return round(imc, 2)


def clasificar_imc(imc):
    # Clasifica el IMC según los rangos dados
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main():
    # Pedir datos al usuario
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    # Calcular IMC
    imc = calcular_imc(peso, altura)

    # Clasificar IMC
    clasificacion = clasificar_imc(imc)

    # Mostrar resultado
    print(f"Tu IMC es {imc} y tu clasificación es: {clasificacion}")



main()