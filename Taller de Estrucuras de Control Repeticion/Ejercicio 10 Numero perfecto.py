#Ejercicio 10 Numero perfecto
numero = int(input("Ingrese un número entero positivo: "))
divisores = ()
suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        divisores += (i,)
        suma_divisores += i
print("Divisores propios de", numero, ":", divisores)
print("Suma de divisores:", suma_divisores)
if suma_divisores == numero:
    print(numero, "es un número perfecto.")
else:
    print(numero, "no es un número perfecto.")
