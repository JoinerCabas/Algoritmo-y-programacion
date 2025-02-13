Algoritmo Ejercicio_9_Salario_Neto
//Entradas
Escribir "Numero de horas trabajadas: "
Leer NumHoras
Escribir "Valor por hora trabajada: "
Leer ValorHora
//Caja Negra
tasaImpuesto <- 0.20 
SueldoBase <- NumHoras * ValorHora
Descuento <- SueldoBase * tasaImpuesto
SalarioNeto <- SueldoBase - Descuento
//Salidas
Escribir "El Sueldo Base es: ", SueldoBase
Escribir "El descuento por impuestos es: ", Descuento
Escribir "El Salario Neto es: ", SalarioNeto
FinAlgoritmo