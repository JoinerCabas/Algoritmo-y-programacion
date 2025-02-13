Algoritmo Ejercicio_19_Lote_de_naranjas
	// Entrada
    Escribir "Cantidad total de naranjas: "
    Leer CantidadNaranjas
    Escribir "Precio por docena de naranjas en Bs: "
    Leer PrecioNaranjas
    Escribir "Monto total obtenido tras la venta: "
    Leer Monto
	//Caja Negra
    Costo <- (CantidadNaranjas/ 12) * PrecioNaranjas
    Ganancia <-Monto- Costo
    PorcentajeGanancia <- (Ganancia / Costo) * 100
    // Salida
    Escribir "El porcentaje de ganancia obtenida es: ", PorcentajeGanancia, "%"
FinAlgoritmo