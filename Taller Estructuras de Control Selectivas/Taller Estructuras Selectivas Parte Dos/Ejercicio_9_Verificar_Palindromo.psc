Algoritmo Ejercicio_9_Verificar_Palindromo
Escribir "Ingrese un número entero:"
 Leer num
		numOriginal <- num 
		reverso <- 0  
		
		Mientras num > 0 Hacer
			digito <- num MOD 10  
			reverso <- reverso * 10 + digito 
			num <- Trunc(num / 10) 
		FinMientras
		Si numOriginal = reverso Entonces
			Escribir "Es un palíndromo"
		Sino
			Escribir "No es un palíndromo"
		FinSi
FinAlgoritmo
