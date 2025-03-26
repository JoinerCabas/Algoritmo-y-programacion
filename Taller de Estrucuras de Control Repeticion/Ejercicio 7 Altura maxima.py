#Ejercicio 7 Altura maxima
N= int(input("Ingrese el numero de estudiantes: "))
max_altura = 0
for _ in range(N):
    altura = float(input("Ingrese la altura del estudiante: "))
    if altura > max_altura:
        max_altura = altura

print("La mayor altura es:", max_altura)