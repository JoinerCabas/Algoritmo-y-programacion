cantidad = int(input("ingrese la cantidad entera en COP: "))

cantidad = (cantidad // 10) * 10

billetes_y_monedas = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

desglose = []

for valor in billetes_y_monedas:
    if cantidad >= valor:
        cantidad_unidades = cantidad // valor
        cantidad -= cantidad_unidades * valor
        desglose.append((valor, cantidad_unidades))

print("Desglose de la cantidad en billetes y monedas:")
for valor, cantidad_unidades in desglose:
    print(str(valor) + " COP: " + str(cantidad_unidades))