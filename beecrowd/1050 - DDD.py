ddd_destinos = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}
codigo = int(input())
if codigo in ddd_destinos:
    print(ddd_destinos[codigo])
else:
    print("DDD nao cadastrado")