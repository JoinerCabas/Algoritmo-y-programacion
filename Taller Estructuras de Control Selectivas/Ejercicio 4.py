piezas=int(input("ingrese el numero de piesas: "))
r=int(piezas*50000)
print("el valor total de la compra es: ", r ")
if (r>=5000000):
    empresa=r*0.55
    banco=r*0.30
    credito=r*0.15
    interes=credito*0.20
    print("la empresa tendra que invertir: ", empresa )
    print("el banco le presta: ", banco)
    print("el valor del credito del fabricante: ", credito y el interes a pagar es: ", interes)

elif(r < 5000000):
    empresa=r*0.70
    banco=r*0.30
    print("la empresa tendra que invertir: ", empresa)
    print("el banco le presta: ", banco)