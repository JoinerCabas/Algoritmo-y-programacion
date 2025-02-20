# Entradas
chelines_austriacos = int(input("Cantidad en chelines austriacos: "))
dracmas_griegos = int(input("Cantidad en dracmas griegos: "))
pesetas = int(input("Cantidad en pesetas: "))
# Caja Negra
pesetas_de_chelines = (chelines_austriacos * 956.871) / 100 
pesetas_de_dracmas = (dracmas_griegos * 88.607) / 100  
francos_franceses = pesetas_de_dracmas / 20.110
dolares = pesetas / 122.499  
liras_italianas = pesetas / (9.289 / 100) 
# Salidas
print("La Cantidad en pesetas es:", pesetas_de_chelines)
print("La Cantidad en francos franceses es:", francos_franceses)
print("La Cantidad en dólares es:", dolares)
print("La Cantidad en liras italianas es:", liras_italianas)