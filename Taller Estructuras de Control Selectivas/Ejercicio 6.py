A= int(input("ingrese A: "))
B= int(input("ingrese B: "))
C= int(input("ingrese C: "))
D= int(input("ingrese D: "))

N = (A * 1000 + B * 100 + C*10 + D) 
if(C >= 5):
    redondear = math.ceil(N / 100) * 100
    print("redondeo: ", redondear)
else:
    redondear = math.floor(N / 100) * 100
    print("redondeo: ", redondear)
    