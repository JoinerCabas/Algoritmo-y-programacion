import math
# Entradas
a = int(input("Ingrese la longitud del lado a: "))
b = int(input("Ingrese la longitud del lado b: "))
c = int(input("Ingrese la longitud del lado c: "))
# Caja Negra
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# Salida
print("El área del triángulo es:", area)