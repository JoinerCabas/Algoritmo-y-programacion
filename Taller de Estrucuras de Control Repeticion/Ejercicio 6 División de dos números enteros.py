#Ejercicio 6 División de dos números enteros 
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0
residuo = dividendo
while residuo >= divisor:
    residuo -= divisor
    cociente += 1
print("Cociente:", cociente)
print("Residuo:", residuo)