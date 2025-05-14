positivos = []
for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos.append(valor)
cantidad = len(positivos)
promedio = sum(positivos) / cantidad
print(f"{cantidad} valores positivos")
print(f"{promedio:.1f}")