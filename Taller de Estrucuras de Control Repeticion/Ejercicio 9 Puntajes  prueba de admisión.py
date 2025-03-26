#Ejercicio 9 Puntajes  prueba de admisión
estudiantes = ()
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    puntaje = float(input("Ingrese el puntaje del estudiante: "))
    
    estudiantes = estudiantes + ((nombre, puntaje),)
    
    continuar = input("¿Desea ingresar otro estudiante? (Si/No): ")
    if continuar != "si":
        break
if estudiantes:
    estudiante_max = ("", float('-inf'))
    estudiante_min = ("", float('inf'))
    total_puntos = 0
    contador = 0
    inferiores = 0
    superiores = 0
    total_estudiantes = 0
    for estudiante in estudiantes:
        nombre, puntaje = estudiante
        if puntaje > estudiante_max[1]:
            estudiante_max = (nombre, puntaje)
        if puntaje < estudiante_min[1]:
            estudiante_min = (nombre, puntaje)
        total_puntos += puntaje
        contador += 1
        total_estudiantes += 1
    promedio = total_puntos / contador
    for _, puntaje in estudiantes:
        if puntaje < promedio:
            inferiores += 1
        elif puntaje > promedio:
            superiores += 1
    porcentaje_inferiores = (inferiores / total_estudiantes) * 100
    porcentaje_superiores = (superiores / total_estudiantes) * 100
    print("Estudiante con el puntaje más alto:", estudiante_max[0], "con", estudiante_max[1])
    print("Estudiante con el puntaje más bajo:", estudiante_min[0], "con", estudiante_min[1])
    print("Puntaje máximo obtenido:", estudiante_max[1])
    print("Puntaje mínimo obtenido:", estudiante_min[1])
    print("Promedio de puntajes:", promedio)
    print("Porcentaje de estudiantes con puntajes inferiores al promedio:", porcentaje_inferiores, "%")
    print("Porcentaje de estudiantes con puntajes superiores al promedio:", porcentaje_superiores, "%")
else:
    print("No se ingresaron datos de estudiantes.")