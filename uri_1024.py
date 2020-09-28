# Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições 
# para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' 
# e assim sucessivamente. 
# Na segunda passada, a linha deverá ser invertida. 
# Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados
# uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”.
# O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento
# dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# a	97
# d	100
# y	121
# |	124

def criptografia (y):
    cont = 0
    for j in range(0, len(y)):
        palavra = y[j]
        lista = list(palavra)
        if (lista[0:8] == 'Texto #3') and cont == 0:
            lista[0:8] =  'Wh{wr #3'
            cont +=1
        elif (lista[0:8] == 'Texto #3') and cont == 1:
            lista[0:8] =  '3# rw{hW'
            cont +=1
        elif (lista[0:8] == 'Texto #3') and cont == 2:
            lista[0:8] =  '3# rvzgV'
            cont +=1
        if cont == 0:
            for i in range(0, len(palavra)):
                posicao = ord(palavra[i]) + 3
                lista[i] = chr(posicao)
        elif len(lista) > len(lista[0,8]):
             for i in range(8, len(palavra)):
                posicao = ord(palavra[i]) + 3
                lista[i] = chr(posicao)
        lista  = lista[::-1]
        palavra = lista[:]
        y[0] = palavra
    return y

def main():   

    lista_palavras = []
    n = int(input())

    for i in range(0 , n):
        frase = input()
        lista_palavras.append(frase)

        print(f'{criptografia(lista_palavras)[i]}')
main();