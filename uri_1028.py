# Ricardo e Vicente são aficionados por figurinhas. Nas horas vagas, eles arrumam um jeito de jogar um “bafo”
# ou algum outro jogo que envolva tais figurinhas. Ambos também têm o hábito de trocarem as figuras repetidas
# com seus amigos e certo dia pensaram em uma brincadeira diferente. Chamaram todos os amigos e propuseram o
# seguinte: com as figurinhas em mãos, cada um tentava fazer uma troca com o amigo que estava mais perto seguindo
# a seguinte regra: cada um contava quantas figurinhas tinha. Em seguida, eles tinham que dividir as figurinhas de
# cada um em pilhas do mesmo tamanho, no maior tamanho que fosse possível para ambos. Então, cada um escolhia uma
# das pilhas de figurinhas do amigo para receber. Por exemplo, se Ricardo e Vicente fossem trocar as figurinhas e
# tivessem respectivamente 8 e 12 figuras, ambos dividiam todas as suas figuras em pilhas de 4 figuras 
# (Ricardo teria 2 pilhas e Vicente teria 3 pilhas) e ambos escolhiam uma pilha do amigo para receber.

# A primeira linha da entrada contém um único inteiro N (1 ≤ N ≤ 3000), indicando o número de casos de teste.
# Cada caso de teste contém 2 inteiros F1 (1 ≤ F1 ≤ 1000) e F2 (1 ≤ F2 ≤ 1000) 
# indicando, respectivamente, a quantidade de figurinhas que Ricardo e Vicente têm para trocar.

f = []
mdc = []

n = int(input())
for i in range(0, n):
    f1, f2 = input().split()
    f1 = int(f1)
    f2 = int(f2)
    f.append(f1)
    f.append(f2)

tamanho = len(f)

for j in range(0, tamanho, 2):
    k = j + 1
    for k in range(k, k + 1):
        maior = 0
        if f[j] > f[j+1]:
            maior = f[j]
        elif f[j] < f[j+1]:
            maior = f[j+1]
        for maior in range(maior, 1, -1):
            if ((f[j] % maior == 0) and (f[j+1] % maior == 0)):
                result = f[j] / maior
                mdc.append(maior)
                result = f[j+1] / maior
                mdc.append(maior)
                break

    print(f'{mdc[j]}')