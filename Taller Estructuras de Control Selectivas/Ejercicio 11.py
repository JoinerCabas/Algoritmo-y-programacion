t=int(input("ingrese la temperatura "))
d=""#deporte
if(t>85):
    d="Natacion"
elif(t>70 and t<=85):
    d="tenis"
elif(t>35 and t<=70):
    d="golf"
elif(t>10 and t<=32):
    d="esqui"
elif(t>0 and t<=10):
    d="marcha"
else:
    d="la temperatura no corresponde a ningun deporte"
#salida
print("el deporte a practicar es:", d )