Algoritmo Ejercicio_16_Galones_de_Gasolina
	// Entradas
    Escribir "Cantidad de galones surtidos: "
    Leer Galones
    // Caja Negra
	GalonaLitro <- 3.785
    PrecioLitro <- 50000 
    Litros <- Galones * GalonaLitro
    MontoTotal <- Litros * PrecioLitro
    // Salida
    Escribir "Cantidad de litros surtidos: ", Litros
    Escribir "Total a pagar: ", MontoTotal, " COP"
FinAlgoritmo
