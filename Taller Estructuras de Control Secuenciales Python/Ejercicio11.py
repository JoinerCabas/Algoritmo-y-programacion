# Entradas
nombre_trabajador = input("Nombre del trabajador: ")
horas_normales = int(input("Número de horas normales trabajadas: "))
pago_hora_normal = int(input("Pago por hora normal: "))
horas_extras = int(input("Número de horas extras trabajadas: "))
numero_hijos = int(input("Número de hijos del trabajador: "))
# Caja Negra
pago_hora_extra = pago_hora_normal * 1.25
sueldo_base = (horas_normales * pago_hora_normal) + (horas_extras * pago_hora_extra)
asignaciones = 250000 + (173000 * numero_hijos) + 180000
deduction_pag_forzoso = sueldo_base * 0.05
deduction_pol_habitacional = sueldo_base * 0.02
deduction_caja_ahorro = sueldo_base * 0.07
total_deducciones = deduction_pag_forzoso + deduction_pol_habitacional + deduction_caja_ahorro
sueldo_neto = sueldo_base + asignaciones - total_deducciones
# Salidas
print("\nResultados:")
print("Nombre del trabajador:", nombre_trabajador)
print("Sueldo Base:", sueldo_base)
print("Asignaciones:", asignaciones)
print("Deducciones:", total_deducciones)
print("Sueldo Neto:", sueldo_neto)