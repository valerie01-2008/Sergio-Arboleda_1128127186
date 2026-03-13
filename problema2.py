# Saldo inicial
saldo = 1000

# Bucle infinito
while True:
    # Mostrar menú
    print("\n--- Cajero Automático ---")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    # Pedir opción al usuario
    opcion = input("Elige una opción (1-4): ")
    
    # Ver saldo
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    
    # Depositar dinero
    elif opcion == "2":
        deposito = input("Ingresa el monto a depositar: ")
        if deposito.isdigit():  # Validar que sea un número positivo
            saldo += int(deposito)
            print(f"Has depositado ${deposito}. Nuevo saldo: ${saldo}")
        else:
            print("Por favor ingresa un monto válido.")
    
    # Retirar dinero
    elif opcion == "3":
        retiro = input("Ingresa el monto a retirar: ")
        if retiro.isdigit():
            retiro = int(retiro)
            if retiro <= saldo:
                saldo -= retiro
                print(f"Has retirado ${retiro}. Nuevo saldo: ${saldo}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Por favor ingresa un monto válido.")
    
    # Salir
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break  # Sale del bucle infinito
    
    # Opción inválida
    else:
        print("Opción no válida. Intenta de nuevo.")