Algoritmo Ejercicio_2_Invercion_de_capital_en_dos_porciento
	//Entrada
    Escribir "Ingrese el capital a invertir:"
    Leer capital
	//Caja Negra
	tasa <- 0.02 
    interes <- capital * tasa
    montoFinal <- capital + interes
	//Salidas
    Escribir "El interés ganado en un mes es: ", interes
    Escribir "El monto final después de un mes es: ", montoFinal
FinAlgoritmo