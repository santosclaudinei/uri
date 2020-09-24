# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após,
# calcule e mostre o valor a ser pago.

codigo1, numero_pecas1, valor_pecas1  = input().split()
codigo2, numero_pecas2, valor_pecas2  = input().split()
valor = float(valor_pecas1) * int(numero_pecas1) + float(valor_pecas2) * int(numero_pecas2)
print(f'VALOR A PAGAR: R$ {valor:.2f}')
