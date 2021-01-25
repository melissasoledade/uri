# URI 1018
# Cédulas: ler valor e verificar menor número de cédulas possível (por nota)

num = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
num = num + 0.001

print("NOTAS:")
for i in notas:
	notas = num//i
	print('{} nota(s) de R$ {:.2f}'.format(int(notas), round(i,2)))	
	num %= i

print("MOEDAS:")
for i in moedas:
	moedas = num//i
	print('{} moeda(s) de R$ {:.2f}'.format(int(moedas), round(i,2)))
	num%=i
