# URI 1048
# Calcular aumento de salário dos funcionários

salario = float(input())
reajuste = 0
percentual = ""

if(salario >= 0.00 and salario <= 400.00):
	reajuste = 0.15*salario
	salario = salario + reajuste
	percentual = "15 %"
elif(salario >= 400.01 and salario <= 800.00):
	reajuste = 0.12*salario
	salario = salario + reajuste
	percentual = "12 %"
elif(salario >= 800.01 and salario <= 1200.00):
	reajuste = 0.10*salario
	salario = salario + reajuste
	percentual = "10 %"
elif(salario >= 1200.01 and salario <= 2000.00):
	reajuste = 0.07*salario
	salario = salario + reajuste
	percentual = "7 %"
else:
	reajuste = 0.04*salario
	salario = salario + reajuste
	percentual = "4 %"

print("Novo salario: %.2f" %salario)
print("Reajuste ganho: %.2f" %reajuste)
print("Em percentual: %s" %percentual)