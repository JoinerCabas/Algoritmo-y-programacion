Algoritmo Ejercicio_8_Calificacion_de_estudiante
	Escribir "Ingrese Calificacion"
	Leer Nota
	Si Nota >= 90 Entonces
		Escribir "A"
	SiNo
		Si Nota >= 80 y Nota < 90 Entonces
			Escribir "B"
		SiNo
			Si Nota >= 70 y Nota < 80 Entonces
				Escribir "C"
			SiNo
				Si Nota >= 60 y Nota < 70 Entonces
					Escribir "D"
				SiNo
					Si Nota < 60  Entonces
						Escribir "F"
					SiNo
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
