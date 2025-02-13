Algoritmo Ejercicio_8_área_de_un_Triángulo
	//Entradas
	Escribir "Ingrese la longitud del lado a:"
    Leer a
    Escribir "Ingrese la longitud del lado b:"
    Leer b
    Escribir "Ingrese la longitud del lado c:"
    Leer c
	//Caja Negra
    s <- (a + b + c) / 2
    area <- Raiz(s * (s - a) * (s - b) * (s - c))
	//Salida
    Escribir "El área del triángulo es: ", area
FinAlgoritmo