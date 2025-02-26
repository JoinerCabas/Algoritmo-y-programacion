cliente=input("ingresa el nombre del cliente: ")
compra=int(input("ingresa el precio de la compra: "))
if (compra>=50000 and compra<100000):
    descuento=compra*0.05
    total=compra-descuento
    print("nombre del cliente: ",cliente)
    print("el descuento es de: ", descuento)
    print("el total a pagar es de: ",total)
elif (compra>=100000 and compra<700000):
    descuento=compra*0.11
    total=compra-descuento
    print("nombre del cliente: ",cliente)
    print("el descuento es de: ", descuento)
    print("el total a pagar es de: ", total)
elif (compra>=700000 and compra<1500000):
    descuento=compra*0.18
    total=compra-descuento
    print("nombre del cliente: ",cliente)
    print("el descuento es de: ", descuento)
    print("el total a pagar es de: ", total)
elif (compra>=1500000):
    descuento=compra*0.25
    total=compra-descuento
    print("nombre del cliente: ",cliente)   
    print("el descuento es de: ", descuento)
    print("el total a pagar es de: ", total)
else:
    (compra<50000)
    print("no se aplica descuento")