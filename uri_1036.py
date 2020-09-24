# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de numero negativo.

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = B ** 2 - 4 * A * C
if(delta >= 0) and (A != 0):
    x1 = (- B + (delta ** (1/2))) / (2 * A)
    x2 = (- B - (delta ** (1/2))) / (2 * A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
else:
    print('Impossivel calcular')