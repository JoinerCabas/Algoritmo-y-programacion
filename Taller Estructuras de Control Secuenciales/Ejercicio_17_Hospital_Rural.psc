Algoritmo Ejercicio_17_Hospital_Rural
	//Entradas
	Escribir "Cantidad de presupuesto del Hopital"
	Leer PresupuestoTotal
	//Caja Negra
	PorcentajeGinecologia<- 40 / 100
    PorcentajeTraumatologia <- 30 / 100
    PorcentajePediatria <- 30 / 100
    PresupuestoGinecologia <- PresupuestoTotal * PorcGinecologia
    PresupuestoTraumatologia <- PresupuestoTotal * PorcTraumatologia
    PresupuestoPediatria <- PresupuestoTotal * PorcPediatria
    // Salida
    Escribir "Presupuesto asignado a Ginecolog�a: ", PresupuestoGinecologia
    Escribir "Presupuesto asignado a Traumatolog�a: ", PresupuestoTraumatologia
    Escribir "Presupuesto asignado a Pediatr�a: ", PresupuestoPediatria
FinAlgoritmo