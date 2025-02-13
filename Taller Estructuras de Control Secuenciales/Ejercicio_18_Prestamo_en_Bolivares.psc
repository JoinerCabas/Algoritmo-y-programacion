Algoritmo Ejercicio_18_Prestamo_en_Bolivares
	//Entrada
	Escribir "Cantidad del Prestamo"
	Leer Prestamo
	Escribir "Cantidad de Intereses Pagados"
	Leer Intereses
	//Caja Negra
	tiempo<- 4 
	TasaAnual<-(Prestamo/(Intereses * tiempo)) *100
	// Salida
    Escribir "La tasa de interés anual fue de: ", TasaAnual, "%"
FinAlgoritmo
