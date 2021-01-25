# Ler hora inicial e final de um jogo e calcular sua duração
# URI 1046

list = input().split()
inicio = int(list[0])
fim = int(list[1])
count = inicio
jogo = 0

if(inicio > fim or inicio == fim):
	while(count < 24 ):
		jogo += 1
		count += 1
	jogo += fim
else:
	for i in range(inicio, fim):
		jogo += 1

print("O JOGO DUROU %d HORA(S)" %jogo)