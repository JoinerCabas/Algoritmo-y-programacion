Algoritmo Ejercicio_9_Verificar_Palindromo
Escribir "Ingrese un n�mero entero:"
 Leer num
		numOriginal <- num 
		reverso <- 0  
		
		Mientras num > 0 Hacer
			digito <- num MOD 10  
			reverso <- reverso * 10 + digito 
			num <- Trunc(num / 10) 
		FinMientras
		Si numOriginal = reverso Entonces
			Escribir "Es un pal�ndromo"
		Sino
			Escribir "No es un pal�ndromo"
		FinSi
FinAlgoritmo
