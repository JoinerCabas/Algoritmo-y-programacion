categoria=int(input("Introduce la categoria del trabajador: "))
sueldo=float(input("Introduce el sueldo del trabajador: "))

aumento = 0

if (categoria == 1  ):
    aumento = sueldo * 0.10

elif (categoria == 2 ):
    aumento = sueldo * 0.15
   
elif (categoria == 3):
    aumento = sueldo * 0.20
   
elif (categoria == 4):
    aumento = sueldo * 0.40
   
elif (categoria == 5):
    aumento = sueldo * 0.60

sueldo_nuevo = aumento + sueldo 

print(f"La categoria del trabajador es:", categoria)
print(f"El sueldo del trabajador es: ", sueldo)
print(f"El aumento del trabajador es: ", aumento )
print(f"El sueldo nuevo del trabajador es: ", sueldo_nuevo)