Algoritmo Ejercicio_9_Verificar_Palindromo
	Escribir "Ingrese palabra:"
	Leer palabra
	long=Longitud(palabra)
	palabra_inversa=""
	Para i<-long Hasta 1 Con Paso -1 Hacer
		palabra_inversa =palabra_inversa + SubCadena(palabra,i,i)
	Fin Para
	Si palabra=palabra_inversa Entonces
		Escribir "Es un polidromo"
	SiNo
		Escribir "No es un polidromo"
	Fin Si
FinAlgoritmo