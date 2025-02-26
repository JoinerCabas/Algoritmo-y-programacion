P = int(input("ingrese el valor de P: "))
Q = int(input("ingrese el valor de Q: "))

expresion = (P ** 3) + (Q ** 4) - (2 * (P ** 2))

if expresion > 680:
    resultado = "P y Q satisfacen la expresión"
else:
    resultado = "P y Q no satisfacen la expresión"
print(resultado + ": P = " + str(P) + ", Q = " + str(Q))