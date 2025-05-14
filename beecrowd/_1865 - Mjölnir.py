C = int(input())
for _ in range(C):
    entrada = input().split()
    nombre = entrada[0]
    fuerza = int(entrada[1])
    if nombre == "Thor":
        print("Y")
    else:
        print("N")