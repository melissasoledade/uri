# URI 1042 teste python
# Ler valores, imprimir em ordem crescente, linha em branco, ordem em que foram lidos

def ler_numeros():
	list = input().split()
	#x, y, z = int(list[0]), int(list[1]), int(list[2])
	list = [int(list[0]), int(list[1]), int(list[2])]
	return list

def imprime_list(list):
	for i in range(0, len(list)):
		print(list[i])


if(__name__ == "__main__"):
	list = ler_numeros()
	list_sorted = sorted(list)
	

	imprime_list(list_sorted)
	print()
	imprime_list(list)