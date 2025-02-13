Algoritmo Ejercicio_5_Calificacion_Alumno
	//Entrada
	Escribir "Nota parcial 1: "
	Leer NotaParcial1
	Escribir "Nota parcial 2: "
	Leer NotaParcial2
	Escribir "Nota parcial 3: "
	Leer NotaParcial3
	Escribir "Nota del examen final: "
	Leer NotaExamenFinal
	Escribir "Nota trabajo final: "
	Leer NotaTrabajoFinal
	//Caja Negra
	tasaParciales <- 0.55
	tasaExamenFinal <- 0.30
	tasaTrabajoFinal <- 0.15
	PromedioParciales <-  (NotaParcial1 + NotaParcial2 + NotaParcial3) / 3 
	PromedioExamenFinal <- NotaExamenFinal * tasaExamenFinal
	PromedioTrabajoFinal <- NotaTrabajoFinal * tasaTrabajoFinal 
	NotaFinal <- (PromedioParciales * tasaParciales) + PromedioExamenFinal  + PromedioTrabajoFinal
	//Salida
	Escribir "La calificacion final de la materia de computacion es: " , NotaFinal
FinAlgoritmo
