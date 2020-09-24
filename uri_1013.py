# Faça um programa que leia três valores e apresente o maior dos três valores
# lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# MaiorAB = ((a+b+abs(a-b))/2)

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
# Um segundo passo, portanto é necessário para chegar no resultado esperado.

A, B, C = input().split()
maior1 = ((int(A) + int(B)) + (abs(int(A) - int(B)))) / 2
maior2 = ((int(maior1) + int(C)) + (abs(int(maior1) - int(C)))) / 2
print(f'{int(maior2)} eh o maior')