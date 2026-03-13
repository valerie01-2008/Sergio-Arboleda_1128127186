import random

# Opciones posibles
opciones = ["piedra", "papel", "tijera"]

# Contadores
victorias_usuario = 0
victorias_maquina = 0

while True:
    # Pedir elección al usuario
    eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    if eleccion_usuario == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    
    if eleccion_usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la máquina
    eleccion_maquina = random.choice(opciones)
    print(f"La máquina eligió: {eleccion_maquina}")
    
    # Determinar el ganador
    if eleccion_usuario == eleccion_maquina:
        print("¡Empate!")
    elif (
        (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or
        (eleccion_usuario == "tijera" and eleccion_maquina == "papel") or
        (eleccion_usuario == "papel" and eleccion_maquina == "piedra")
    ):
        print("¡Ganaste!")
        victorias_usuario += 1
    else:
        print("¡Gana la máquina!")
        victorias_maquina += 1
    
    # Mostrar contador de victorias
    print(f"Marcador -> Usuario: {victorias_usuario}, Máquina: {victorias_maquina}")