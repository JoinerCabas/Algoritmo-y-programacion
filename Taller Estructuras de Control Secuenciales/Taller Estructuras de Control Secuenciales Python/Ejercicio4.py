# Entrada
total_compra = int(input("Ingrese total de la compra: "))
# Caja Negra
tasa_descuento = 0.15
descuento = total_compra * tasa_descuento
total_pagar = total_compra - descuento
# Salidas
print("El Descuento aplicado es:", descuento)
print("El total a pagar después del descuento es:", total_pagar)