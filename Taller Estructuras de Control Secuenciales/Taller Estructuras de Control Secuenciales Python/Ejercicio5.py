# Entrada
nota_parcial1 = int(input("Nota parcial 1: "))
nota_parcial2 = int(input("Nota parcial 2: "))
nota_parcial3 = int(input("Nota parcial 3: "))
nota_examen_final = int(input("Nota del examen final: "))
nota_trabajo_final = int(input("Nota trabajo final: "))
# Caja Negra
tasa_parciales = 0.55
tasa_examen_final = 0.30
tasa_trabajo_final = 0.15
promedio_parciales = (nota_parcial1 + nota_parcial2 + nota_parcial3) / 3 
promedio_examen_final = nota_examen_final * tasa_examen_final
promedio_trabajo_final = nota_trabajo_final * tasa_trabajo_final 
nota_final = (promedio_parciales * tasa_parciales) + promedio_examen_final + promedio_trabajo_final
# Salida
print("La calificación final de la materia de computación es:", nota_final)