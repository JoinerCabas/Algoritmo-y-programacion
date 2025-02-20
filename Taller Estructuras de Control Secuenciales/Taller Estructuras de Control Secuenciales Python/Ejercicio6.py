#Entradas
Mujeres=int(input("ingrese cantidad de mujeres: "))
Hombres=int(input("ingrese cantidad de Hombres: "))
#Caja Negra
Total_Estudiantes=Mujeres+Hombres
Por_Mujeres=Mujeres/(Total_Estudiantes*100)
Por_Hombres=Hombres/(Total_Estudiantes*100)
#Salidas
print( "El porcentje de Mujeres es: " ,Por_Mujeres, "%", "El porcentje de hombres es: " ,Por_Hombres, "%")