# URI 1049
# Classificação dos animais por 3 palavras

vert = input()
classe = input()
tipo = input()

if(vert == "vertebrado"):
	if(classe == "ave"):
		if(tipo == "carnivoro"):
			print("aguia")
		else:
			print("pomba")
	else:
		if(tipo == "onivoro"):
			print("homem")
		else:
			print("vaca")
else:
	if(classe == "inseto"):
		if(tipo == "hematofago"):
			print("pulga")
		else:
			print("lagarta")
	else:
		if(tipo == "hematofago"):
			print("sanguessuga")
		else:
			print("minhoca")