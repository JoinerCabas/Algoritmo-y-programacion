#Ejercicio 5 sumatoria que se aproxime a 1000
suma = 0
k = 1
contador = 0

while suma + k <= 1000:
    suma += k
    contador += 1
    k += 1

print("Numero de términos necesarios:", contador)
