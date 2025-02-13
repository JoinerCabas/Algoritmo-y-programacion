Algoritmo Ejercicio_20_Comerciante_de_computadores
	// Entrada
    Escribir "Precio al contado del computador: "
    Leer Precio
    Escribir "Valor de la cuota mensual: "
    Leer ValorCuota
	//Caja Negra
    TotalCuotas <- ValorCuota * 12
    RecargoTotal <- TotalCuotas - Precio
    PorcentajeRecargo <- (RecargoTotal / Precio) * 100
    // Salida
    Escribir "El porcentaje de recargo por pago en cuotas es: ", PorcentajeRecargo, "%"
FinAlgoritmo
