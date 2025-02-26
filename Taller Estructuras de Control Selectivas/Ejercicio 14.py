#Entradas
LecturaAnterior = int(input("Ingrese la lectura anterior (Kwh): "))
LecturaActual = int(input("Ingrese la lectura actual (Kwh): "))
#Caja Negra
consumo = LecturaActual - LecturaAnterior
if consumo < 0:
    print("Error: La lectura actual debe ser mayor o igual a la lectura anterior.")
else:
    if consumo <= 100:
        costokwh = 4600
    elif consumo <= 300:
        costokwh = 80000
    elif consumo <= 500:
        costokwh = 100000
    else:
        costokwh = 120000
    montoapagar = consumo * costokwh
#Salida
    print("El consumo fue de:", consumo ) 
    print("El monto total a pagar es: ", montoapagar)
