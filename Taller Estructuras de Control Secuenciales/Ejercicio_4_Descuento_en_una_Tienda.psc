Algoritmo Ejercicio_4_Descuento_en_una_Tienda
	//Entrada
	Escribir "Ingrese total de la compra: "
	Leer TotalCompra
	//Caja Negra
	TasaDescuento<-0.15
	Descuento <- TotalCompra * TasaDescuento
	TotalPagar <- TotalCompra - Descuento
	//Salidas
	Escribir "El Descuento aplicado es: ", Descuento
	Escribir "El total a pagar después del descuento es: ", TotalPagar
FinAlgoritmo