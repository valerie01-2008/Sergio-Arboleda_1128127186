import random

usuario_gana = 0
maquina_gana = 0

opciones = ["piedra", "papel", "tijera"]

while True:

    usuario = input("Elige piedra, papel o tijera: ")
    maquina = random.choice(opciones)

    print("La máquina eligió:", maquina)

    if usuario == maquina:
        print("Empate")

    elif usuario == "piedra" and maquina == "tijera":
        print("Ganaste")
        usuario_gana = usuario_gana + 1

    elif usuario == "tijera" and maquina == "papel":
        print("Ganaste")
        usuario_gana = usuario_gana + 1

    elif usuario == "papel" and maquina == "piedra":
        print("Ganaste")
        usuario_gana = usuario_gana + 1

    else:
        print("La máquina gana")
        maquina_gana = maquina_gana + 1

    print("Victorias usuario:", usuario_gana)
    print("Victorias máquina:", maquina_gana)

    jugar = input("¿Quieres jugar otra vez? (s/n): ")

    if jugar == "n":
        break