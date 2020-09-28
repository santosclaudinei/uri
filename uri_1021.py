valor = float(input())
n100 = valor // 100
resto = valor % 100
n50 = resto // 50
resto = resto % 50
n20 = resto // 20
resto = resto % 20
n10 = resto // 10
resto = resto % 10
n05 = (resto // 5)
resto = resto % 5
n02 = resto // 2
resto = resto % 2
m01 = resto // 1
resto = resto % 1
m50 = resto // 0.50
resto = round((resto % 0.50),2)
m25 = resto // 0.25
resto = round((resto % 0.25),2)
m10 = resto // 0.10
resto = round((resto % 0.10),2)
m5 = resto // 0.05
resto = round((resto % 0.05),2)
m1 = resto * 100

print('NOTAS:')
print(f'{n100:.0f} nota(s) de R$ 100,00')
print(f'{n50:.0f} nota(s) de R$ 50,00')
print(f'{n20:.0f} nota(s) de R$ 20,00')
print(f'{n10:.0f} nota(s) de R$ 10,00')
print(f'{n05:.0f} nota(s) de R$ 5,00')
print(f'{n02:.0f} nota(s) de R$ 2,00')
print('MOEDAS:')
print(f'{m01:.0f} moeda(s) de R$ 1,00')
print(f'{m50:.0f} moeda(s) de R$ 0.50')
print(f'{m25:.0f} moeda(s) de R$ 0.25')
print(f'{m10:.0f} moeda(s) de R$ 0.10')
print(f'{m5:.0f} moeda(s) de R$ 0.05')
print(f'{m1:.0f} moeda(s) de R$ 0.01')