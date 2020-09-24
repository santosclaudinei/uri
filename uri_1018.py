'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.'''
'476'
valor = int(input())
n100 = valor // 100
n50 = (valor - (n100 * 100)) // 50
n20 = (valor - (n100 * 100) - (n50 * 50)) // 20
n10 = (valor - (n100 * 100) - (n50 * 50) - (n20 * 20)) // 10
n05 = (valor - (n100 * 100) - (n50 * 50) - (n20 * 20) - (n10 * 10)) // 5
n02 = (valor - (n100 * 100) - (n50 * 50) - (n20 * 20) - (n10 * 10) - (n05 * 5)) // 2
n01 = (valor - (n100 * 100) - (n50 * 50) - (n20 * 20) - (n10 * 10) - (n05 * 5) - (n02 * 2)) // 1

print(valor)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n05} nota(s) de R$ 5,00')
print(f'{n02} nota(s) de R$ 2,00')
print(f'{n01} nota(s) de R$ 1,00')