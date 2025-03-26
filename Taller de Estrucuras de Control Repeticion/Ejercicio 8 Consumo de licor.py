#Ejercicio 8 Consumo de licor
total_encuestados = 0
total_consumen_licor = 0
total_mujeres_menores = 0
total_hombres_sin_aguardiente = 0
total_cerveza = 0
suma_edades_cerveza = 0
total_whisky = 0
while True:
    total_encuestados += 1
    consume = input("¿Consume licor? (Si/No): ")
    if consume == "si":
        total_consumen_licor += 1
        licor = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
    else:
        licor = None
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (M/F): ")
    if sexo == "F" and edad < 18:
        total_mujeres_menores += 1
    if sexo == "M" and licor != 1 and 20 <= edad <= 25:
        total_hombres_sin_aguardiente += 1
    if licor == 3:
        total_cerveza += 1
        suma_edades_cerveza += edad
    if licor == 5:
        total_whisky += 1
    continuar = input("¿Desea continuar con la encuesta? (Si/No): ")
    if continuar != "si":
        break
if total_cerveza > 0:
    promedio_edad_cerveza = suma_edades_cerveza / total_cerveza
else:
    promedio_edad_cerveza = 0
porcentaje_whisky = (total_whisky / total_encuestados) * 100 if total_encuestados > 0 else 0

# Mostrar resultados
print("Total de personas encuestadas que consumen licor:", total_consumen_licor)
print("Total de mujeres menores de edad:", total_mujeres_menores)
print("Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años:", total_hombres_sin_aguardiente)
print("Promedio de edad de quienes consumen cerveza:", promedio_edad_cerveza)
print("Porcentaje de personas que consumen whisky respecto al total encuestado:", porcentaje_whisky, "%")