sueldo_bruto=float(input('Ingrese el nuevo sueldo del trabajador: '))
if sueldo_bruto>900:
    print(sueldo_bruto>900*0.15)
else:
    print(sueldo_bruto<900*0.12)
print(f'Nuevo salario del trabajador: {sueldo_bruto:.2f} COP')