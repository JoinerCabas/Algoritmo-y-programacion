Algoritmo Ejercicio_10_Bolsa_de_Madrid
	//Entradas
    Escribir "Cantidad en chelines austriacos:"
    Leer ChelinesAustríacos
	Escribir "Cantidad en dracmas griegos:"
    Leer DracmasGriegos
	Escribir "Cantidad en pesetas:"
    Leer Pesetas
	//Caja Negra
    PesetasDeChelines <- (ChelinesAustriacos * 956.871) / 100 
	PesetasDeDracmas <- (DracmasGriegos * 88.607) / 100  
    FrancosFranceses <- PesetasDeDracmas / 20.110
	Dolares <- Pesetas / 122.499  
    LirasItalianas <- Pesetas / (9.289 / 100) 
	//Salidas
    Escribir "La Cantidad en pesetas es: ", PesetasDeChelines
    Escribir "La Cantidad en francos franceses es: ", FrancosFranceses
    Escribir "La Cantidad en dolares es: ", Dolares
    Escribir "La Cantidad en liras italianas es: ", LirasItalianas
FinAlgoritmo