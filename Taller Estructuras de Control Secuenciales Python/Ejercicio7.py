# Entrada
num_metros = int(input("Número de Metros: "))
# Caja Negra
total_pulgadas = num_metros * 39.27 
pies = int(total_pulgadas // 12)
pulgadas_restantes = total_pulgadas % 12
# Salida
print("Equivale a:", pies, "pies y", pulgadas_restantes, "pulgadas")