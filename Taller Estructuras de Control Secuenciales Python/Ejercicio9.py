# Entradas
num_horas = int(input("Número de horas trabajadas: "))
valor_hora = int(input("Valor por hora trabajada: "))
# Caja Negra
tasa_impuesto = 0.20 
sueldo_base = num_horas * valor_hora
descuento = sueldo_base * tasa_impuesto
salario_neto = sueldo_base - descuento
# Salidas
print("El Sueldo Base es:", sueldo_base)
print("El descuento por impuestos es:", descuento)
print("El Salario Neto es:", salario_neto)
