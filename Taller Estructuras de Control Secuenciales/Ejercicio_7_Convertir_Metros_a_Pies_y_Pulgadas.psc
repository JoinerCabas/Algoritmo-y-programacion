Algoritmo Ejercicio_7_Convertir_Metros_a_Pies_y_Pulgadas
	//Entrada
	Escribir "Numero de Metros"
	Leer NumMetros
	//Caja Negra
	TotalPulgadas <- NumMetros * 39.27 
	Pies<- (TotalPulgadas / 12)
	PulgadasRestantes <-TotalPulgadas - (pies * 12)
	//Salida
	Escribir "Equivale: " , Pies, "pies y " , PulgadasRestantes ,  "Pulgadas"
FinAlgoritmo
