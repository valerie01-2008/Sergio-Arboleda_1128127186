saldo = 1000

while True:
    print("----- CAJERO AUTOMATICO -----")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print("Tu saldo es:", saldo)

    elif opcion == 2:
        deposito = float(input("Cantidad a depositar: "))
        saldo = saldo + deposito
        print("Deposito realizado. Nuevo saldo:", saldo)

    elif opcion == 3:
        retiro = float(input("Cantidad a retirar: "))
        if retiro <= saldo:
            saldo = saldo - retiro
            print("Retiro realizado. Nuevo saldo:", saldo)
        else:
            print("No tienes suficiente saldo")

    elif opcion == 4:
        print("Gracias por usar el cajero")
        break

    else:
        print("Opcion no valida")