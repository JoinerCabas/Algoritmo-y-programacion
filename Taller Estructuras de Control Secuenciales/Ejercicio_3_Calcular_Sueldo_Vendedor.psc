Algoritmo Ejercicio_3_Calcular_Sueldo_Vendedor
	//Entrada
 Escribir "Ingrese el sueldo base del vendedor:"
    Leer sueldoBase
    Escribir "Ingrese el valor de venta 1: "
    Leer venta1
    Escribir "Ingrese el valor de venta 2: "
    Leer venta2
    Escribir "Ingrese el valor de venta 3: "
    Leer venta3
	//Caja Negra
	tasaComision <- 0.10 
    comision1 <- venta1 * tasaComision
    comision2 <- venta2 * tasaComision
    comision3 <- venta3 * tasaComision
    totalComisiones <- comision1 + comision2 + comision3
    totalRecibido <- sueldoBase + totalComisiones
	//Salidas
    Escribir "La comisión por venta 1 es: ", comision1
    Escribir "La comisión por venta 2 es: ", comision2
    Escribir "La comisión por venta 3 es: ", comision3
    Escribir "El total de comisiones es: ", totalComisiones
    Escribir "El total recibido por el vendedor es: ", totalRecibido
FinAlgoritmo