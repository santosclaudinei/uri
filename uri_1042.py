# Leia 3 valores inteiros e ordene-os em ordem crescente. 
# No final, mostre os valores em ordem crescente, uma linha
# em branco e em seguida, os valores na sequência como foram lidos.

# Entrada - A entrada contem três números inteiros.
# Saída - Imprima a saída conforme foi especificado.

def main():
    
    n1, n2, n3 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if ((n1 > n2) and (n1 > n3)):
        maior = n1
        if (n2 > n3):
            meio = n2
            menor = n3
        elif (n2 < n3):
            meio = n3
            menor = n2
        print(menor)
        print(meio)
        print(maior)
        print('')
        print(n1)
        print(n2)
        print(n3)

    if ((n2 > n1) and (n2 > n3)):
        maior = n2
        if (n1 > n3):
            meio = n1
            menor = n3
        elif (n1 < n3):
            meio = n3
            menor = n1
        print(menor)
        print(meio)
        print(maior)
        print('')
        print(n1)
        print(n2)
        print(n3)

    if ((n3 > n1) and (n3 > n2)):
        maior = n3
        if (n1 > n2):
            meio = n1
            menor = n2
        else:
            meio = n2
            menor = n1
        print(menor)
        print(meio)
        print(maior)
        print('')
        print(n1)
        print(n2)
        print(n3)

main();