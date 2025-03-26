#Ejercicio 11 Cajero Automático
saldo = 1000  
while True:
    print("\nCajero Automático")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ") 
    if opcion == "1":
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print("Depósito exitoso. Saldo actual:", saldo)
        else:
            print("El monto debe ser positivo.")
    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print("Retiro exitoso. Saldo actual:", saldo)
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser positivo.")
    elif opcion == "3":
        print("Saldo actual:", saldo)
    
    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break
    else:
        print("Opción no válida, intente de nuevo.")