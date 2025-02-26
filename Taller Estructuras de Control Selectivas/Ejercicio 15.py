edad = int(input("ingrese la edad en meses (para menores de 1 año) o en años: "))
sexo = input("ingrese el sexo (M para masculino, F para femenino): ")
nivel_hemoglobina = float(input("ingrese el nivel de hemoglobina en g%: "))

resultado = "Negativo"

if edad <= 1:
    if 13 <= nivel_hemoglobina <= 26:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
elif 1 < edad <= 6:
    if 10 <= nivel_hemoglobina <= 18:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
elif 6 < edad <= 12:
    if 11 <= nivel_hemoglobina <= 15:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
elif 12 < edad <= 60:
    if 11.5 <= nivel_hemoglobina <= 15:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
elif 60 < edad <= 120:
    if 12.6 <= nivel_hemoglobina <= 15.5:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
elif 120 < edad <= 180:
    if 13 <= nivel_hemoglobina <= 15.5:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
else:
    if sexo == "F":
        if 12 <= nivel_hemoglobina <= 16:
            resultado = "Negativo"
        else:
            resultado = "Positivo"
    elif sexo == "M":
        if 14 <= nivel_hemoglobina <= 18:
            resultado = "Negativo"
        else:
            resultado = "Positivo"

print(f"Resultado: ", resultado )