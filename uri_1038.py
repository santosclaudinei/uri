# Com base na tabela abaixo, escreva um programa que leia o código de um item 
# e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# 1 - Hot Dog           R$ 4.00
# 2 - X-Salada          R$ 4.50
# 3 - X-Bacon           R$ 5.00
# 4 - Torrada Simples   R$ 2.00
# 5 - Refrigerante      R$ 1.50

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código 
# e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor
#  a ser pago, com 2 casas após o ponto decimal.

def main():

    cod, qtd = input().split()
    cod = int(cod)
    qtd = int(qtd)

    if cod == 1:
        print(f'Total: R$ {qtd * 4.00:.2f}')
    if cod == 2:
        print(f'Total: R$ {qtd * 4.50:.2f}')
    if cod == 3:
        print(f'Total: R$ {qtd * 5.00:.2f}')
    if cod == 4:
        print(f'Total: R$ {qtd * 2.00:.2f}')
    if cod == 5:
        print(f'Total: R$ {qtd * 1.50:.2f}')

main();