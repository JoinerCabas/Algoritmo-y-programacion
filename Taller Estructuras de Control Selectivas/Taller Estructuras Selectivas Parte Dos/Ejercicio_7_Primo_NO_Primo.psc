Algoritmo Ejercicio_7_Primo_NO_Primo
	Escribir "Ingrese un número entero:"
    Leer N
    
    Si N <= 1 Entonces
        Escribir "No es primo"
	Sino 
		Si N = 2 Entonces
        Escribir "Es primo"
    Sino
        esPrimo <- Verdadero 
        Para i <- 2 Hasta Raiz(num) Hacer
            Si num MOD i = 0 Entonces
                esPrimo <- Falso  
            FinSi
        FinPara
        
        Si esPrimo Entonces
            Escribir "Es primo"
        Sino
            Escribir "No es primo"
        FinSi
    FinSi
fin si 
FinAlgoritmo