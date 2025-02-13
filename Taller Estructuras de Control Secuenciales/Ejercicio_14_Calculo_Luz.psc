Algoritmo Ejercicio_14_Calculo_Luz
    // Entradas
    Escribir "Lectura anterior del medidor en kilovatio: "
    Leer LecturaAnterior
    Escribir "Lectura actual del medidor en kilovatio: "
    Leer LecturaActual
    Escribir "Costo por kilovatio: "
    Leer CostoPorKilovatio
    // Caja Negra
    Consumo <- LecturaActual - LecturaAnterior
    MontoTotal <- Consumo * CostoPorKilovatio
    // Salida
    Escribir "El consumo de energia electrica fue de: ", Consumo
    Escribir "El monto total a pagar es: ", MontoTotal
FinAlgoritmo