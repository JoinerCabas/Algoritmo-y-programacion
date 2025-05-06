Estudiantes = {}
Max_Estudiantes = 100
for i in range(1, Max_Estudiantes + 1):
    print(f"Estudiante {i}:")
    Nombre = input("  Nombre: ")
    Nota = float(input("  Nota: "))
    Estudiantes[str(i)] = {
        "nombre": Nombre,
        "nota": Nota
    }
    Continuar = input("¿Desea incluir otro estudiante? (si/no): ").lower()
    if Continuar != "si":
        break
Aprobados = []
Suspendidos = []
SumaNotas = 0
for estudiante in Estudiantes.values():
    nota = estudiante["nota"]
    SumaNotas += nota
    if nota >= 5:
        Aprobados.append(estudiante["nombre"])
    else:
        Suspendidos.append(estudiante["nombre"])
media = SumaNotas / len(Estudiantes)
print("RESULTADOS")
print("Aprobados:", Aprobados)
print("Suspendidos:", Suspendidos)
print(f"Nota media de la clase: {media:.2f}")