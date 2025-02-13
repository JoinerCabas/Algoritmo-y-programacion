Algoritmo Ejercicio_15_Descuento_Precio_de_Venta
	// Entradas
    Escribir "Ingrese el precio de venta al publico: "
    Leer PrecioVenta
    Escribir "Ingrese el precio final pagado: "
    Leer PrecioFinal
    // Caja Negra
    Descuento <- ((PrecioVenta - PrecioFinal) / PrecioVenta) * 100
    // Salida
    Escribir "El porcentaje de descuento aplicado es: ", Descuento, "%"
FinAlgoritmo