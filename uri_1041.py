# URI 1041
# Determinar quadrante ou eixo em que o ponto encontra-se

def read():
	list = input().split()
	list = [float(list[0]), float(list[1])]
	return list

def result(list):
	x, y = list[0], list[1]
	res = ""
	if(x > 0 and y > 0):
		res = "Q1"
	elif(x > 0 and y < 0):
		res = "Q4"
	elif(x < 0 and y < 0):
		res = "Q3"
	elif(x < 0 and y > 0):
		res = "Q2"
	elif(x == 0 and y != 0):
		res = "Eixo Y"
	elif(y == 0 and x != 0):
		res = "Eixo X"
	else:
		res = "Origem"
	return res

if(__name__ == "__main__"):
	list = read()
	res = result(list)
	print(res)
