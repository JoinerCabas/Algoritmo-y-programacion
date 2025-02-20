# Entrada
sueldoBase = int(input("Ingrese el sueldo base del vendedor: "))
venta1 = int(input("Ingrese el valor de venta 1: "))
venta2 = int(input("Ingrese el valor de venta 2: "))
venta3 = int(input("Ingrese el valor de venta 3: "))
# Caja Negra
tasaComision = 0.10 
comision1 = venta1 * tasaComision
comision2 = venta2 * tasaComision
comision3 = venta3 * tasaComision
total_Comisiones = comision1 + comision2 + comision3
total_Recibido = sueldoBase + total_Comisiones
# Salidas
print("La comisión por venta 1 es:", comision1)
print("La comisión por venta 2 es:", comision2)
print("La comisión por venta 3 es:", comision3)
print("El total de comisiones es:", total_Comisiones)
print("El total recibido por el vendedor es:", total_Recibido)