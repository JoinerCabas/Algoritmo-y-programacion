monto_inversion=float(input('Cantidad de dinero a invertir '))
interes=float(input('Interes anual '))
reinversion=monto_inversion*interes
if float(monto_inversion>100):
    print('La cantidad de dinero invertida es mayor a 100')
else:
    print('La cantidad de dinero no invertiva es igual a 0')
print('El interes anual es de: ', reinversion)