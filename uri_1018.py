# URI 1018
# Cédulas: ler valor e verificar menor número de cédulas possível (por nota)

num = int(input())
print(num)
print("%d nota(s) de R$ 100,00" %int(num/100))
num = num%100
print("%d nota(s) de R$ 50,00" %int(num/50))
num = num%50
print("%d nota(s) de R$ 20,00" %int(num/20))
num = num%20
print("%d nota(s) de R$ 10,00" %int(num/10))
num = num%10
print("%d nota(s) de R$ 5,00" %int(num/5))
num = num%5
print("%d nota(s) de R$ 2,00" %int(num/2))
num = num%2
print("%d nota(s) de R$ 1,00" %int(num/1))
