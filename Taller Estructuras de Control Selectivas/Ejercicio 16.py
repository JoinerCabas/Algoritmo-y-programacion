A = float(input("ingrese el valor de A: "))
B = float(input("ingrese el valor de B: "))
C = float(input("ingrese el valor de C: "))
D = B**2 - 4*A*C
if D > 0:
    X1 = (-B + (D)**0.5) / (2*A)
    X2 = (-B - (D)**0.5) / (2*A)
    print("La ecuación tiene dos soluciones reales:")
    print("X1 =", X1)
    print("X2 =", X2)
elif D == 0:
    X1 = X2 = -B / (2*A)
    print("La ecuación tiene una única solución real:")
    print("X1 = X2 =", X1)
else:
    print("La ecuación no tiene solución en los números reales.")