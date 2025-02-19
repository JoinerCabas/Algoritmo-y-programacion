# Entradas
examen_matematica = int(input("Nota examen de Matemática: "))
tarea1_matematica = int(input("Nota de la tarea 1 de Matemática: "))
tarea2_matematica = int(input("Nota de la tarea 2 de Matemática: "))
tarea3_matematica = int(input("Nota de la tarea 3 de Matemática: "))
examen_fisica = int(input("Nota del examen de Física: "))
tarea1_fisica = int(input("Nota de la tarea 1 de Física: "))
tarea2_fisica = int(input("Nota de la tarea 2 de Física: "))
examen_quimica = int(input("Nota del examen de Química: "))
tarea1_quimica = int(input("Nota de la tarea 1 de Química: "))
tarea2_quimica = int(input("Nota de la tarea 2 de Química: "))
tarea3_quimica = int(input("Nota de la tarea 3 de Química: "))
# Caja Negra
promedio_matematica = (0.9 * examen_matematica) + (0.1 * ((tarea1_matematica + tarea2_matematica + tarea3_matematica) / 3))
promedio_fisica = (0.8 * examen_fisica) + (0.2 * ((tarea1_fisica + tarea2_fisica) / 2))
promedio_quimica = (0.85 * examen_quimica) + (0.15 * ((tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3))
promedio_general = (promedio_matematica + promedio_fisica + promedio_quimica) / 3
# Salidas
print("Promedio de Matemática:", promedio_matematica)
print("Promedio de Física:", promedio_fisica)
print("Promedio de Química:", promedio_quimica)
print("Promedio General:", promedio_general)
