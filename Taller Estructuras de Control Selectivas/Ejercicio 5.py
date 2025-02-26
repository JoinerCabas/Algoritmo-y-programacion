D1=int(input("ingrese el valor total del departamente de ventas1:  "))
D2=int(input("ingrese el valor total del departamente de ventas2:  "))
D3=int(input("ingrese el valor total del departamente de ventas3:  "))
recaudo_esperado = 2000000 * 0.33
recaudo_total = (D1+D2+D3)
print("el recaudo total de la empresa es: COP(recaudo_total)")
comisicion = 0.33 * recaudo_esperado
if(recaudo_total > comisicion):
    D1=1300000*0.20
    D2=1300000*0.20
    D3=1300000*0.20
    print("la comisicion total de ventas 1 es: COP (D1+1300000)")  
    print("la comisicion total de ventas 2 es: COP (D2+1300000)")
    print("la comisicion total de ventas 3 es: COP (D3+1300000)")
else:
    recaudo_total < comisicion
    print("no hay comision")