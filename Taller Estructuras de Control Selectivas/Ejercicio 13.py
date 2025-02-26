dia_nacimiento = int(input("ingrese el día de nacimiento: "))
mes_nacimiento = int(input("ingrese el mes de nacimiento: "))
año_nacimiento = int(input("ingrese el año de nacimiento: "))
from datetime import datetime
fecha_actual = datetime.now()
dia_actual = fecha_actual.day
mes_actual = fecha_actual.month
año_actual = fecha_actual.year
edad = año_actual - año_nacimiento
if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad -= 1
if (mes_nacimiento == 11 and dia_nacimiento >= 22) or (mes_nacimiento == 12 and dia_nacimiento <= 21):
    signo_zodiaco = "Sagitario"
elif (mes_nacimiento == 12 and dia_nacimiento >= 22) or (mes_nacimiento == 1 and dia_nacimiento <= 20):
    signo_zodiaco = "Capricornio"
elif (mes_nacimiento == 1 and dia_nacimiento >= 21) or (mes_nacimiento == 2 and dia_nacimiento <= 19):
    signo_zodiaco = "Acuario"
elif (mes_nacimiento == 2 and dia_nacimiento >= 20) or (mes_nacimiento == 3 and dia_nacimiento <= 19):
    signo_zodiaco = "Piscis"
elif (mes_nacimiento == 3 and dia_nacimiento >= 21) or (mes_nacimiento == 4 and dia_nacimiento <= 20):
    signo_zodiaco = "Aries"
elif (mes_nacimiento == 4 and dia_nacimiento >= 21) or (mes_nacimiento == 5 and dia_nacimiento <= 21):
    signo_zodiaco = "Tauro"
elif (mes_nacimiento == 5 and dia_nacimiento >= 22) or (mes_nacimiento == 6 and dia_nacimiento <= 21):
    signo_zodiaco = "Géminis"
elif (mes_nacimiento == 6 and dia_nacimiento >= 22) or (mes_nacimiento == 7 and dia_nacimiento <= 22):
    signo_zodiaco = "Cáncer"
elif (mes_nacimiento == 7 and dia_nacimiento >= 23) or (mes_nacimiento == 8 and dia_nacimiento <= 23):
    signo_zodiaco = "Leo"
elif (mes_nacimiento == 8 and dia_nacimiento >= 24) or (mes_nacimiento == 9 and dia_nacimiento <= 22):
    signo_zodiaco = "Virgo"
elif (mes_nacimiento == 9 and dia_nacimiento >= 23) or (mes_nacimiento == 10 and dia_nacimiento <= 22):
    signo_zodiaco = "Libra"
elif (mes_nacimiento == 10 and dia_nacimiento >= 23) or (mes_nacimiento == 11 and dia_nacimiento <= 21):
    signo_zodiaco = "Escorpión"

print("Signo del zodiaco: " + signo_zodiaco)
print("Edad: " + str(edad) + " años")