Algoritmo Ejercicio_12_Promedio_Materias_Dificiles 
	//Entradas
	Escribir "Nota examen de Matematica:"
    Leer ExamenMatematica
    Escribir "Notas de las tres tareas de Matematica:"
    Leer Tarea1Matematica
    Leer Tarea2Matematica
    Leer Tarea3Matematica
    Escribir "Nota del examen de Fisica:"
    Leer ExamenFisica
    Escribir "Nota de las dos tareas de Fisica:"
    Leer Tarea1Fisica
    Leer Tarea2Fisica
    Escribir "Nota del examen de Quimica:"
    Leer ExamenQuimica
    Escribir "Nota de las tres tareas de Quimica:"
    Leer Tarea1Quimica
    Leer Tarea2Quimica
    Leer Tarea3Quimica
	//Caja Negra
    PromedioMatematica <- (0.9 * ExamenMatematica) + (0.1 * ((Tarea1Matematica + Tarea2Matematica + Tarea3Matematica) / 3))
    PromedioFisica <- (0.8 * ExamenFisica) + (0.2 * ((Tarea1Fisica + Tarea2Fisica) / 2))
    PromedioQuimica <- (0.85 * ExamenQuimica) + (0.15 * ((Tarea1Quimica + Tarea2Quimica + Tarea3Quimica) / 3))
    PromedioGeneral <- (PromedioMatematica + PromedioFisica + PromedioQuimica) / 3
	//Salidas
    Escribir "Promedio de Matematica: ", PromedioMatematica
    Escribir "Promedio de Fisica: ", PromedioFisica
    Escribir "Promedio de Quimica: ", PromedioQuimica
    Escribir "Promedio General: ", PromedioGeneral
FinAlgoritmo 