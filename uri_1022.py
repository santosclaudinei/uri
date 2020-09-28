#include <stdio.h>
 
int main() {
 
    n = int(input())
    lista = []
    lista_sim = []

    for i in range(0, n):
        expressao = input().split()
        N1 = int(expressao[0])
        D1 = int(expressao[2])
        N2 = int(expressao[4])
        D2 = int(expressao[6])
        if (expressao[3]) == '+':
            som_numerador = N1 * D2 + N2 * D1
            lista.append(som_numerador)
            som_denominador = D1 * D2
            lista.append(som_denominador)
        elif (expressao[3]) == '-':
            sub_numerador = N1 * D2 - N2 * D1
            lista.append(sub_numerador)
            sub_denominador = D1 * D2
            lista.append(sub_denominador)
        elif (expressao[3]) == '*':
            multi_numerador = N1 * N2
            lista.append(multi_numerador)
            multi_denominador = D1 * D2
            lista.append(multi_denominador)
        elif (expressao[3]) == '/':
            div_numerador = N1 * D2
            lista.append(div_numerador)
            div_denominador = N2 * D1
            lista.append(div_denominador)
tamanho = len(lista)

    for j in range(0, tamanho, 2):
        k = j + 1
        for k in range(k, k + 1):
            maior = 0
            if (lista[j] > lista[k]):
                maior = lista[j]
            else:
                maior = lista[k]
            for maior in range(maior, 1, -1):
                if ((lista[j] % maior == 0) and (lista[k] % maior == 0)):
                    result = lista[j] / maior
                    lista_sim.append(result)
                    result = lista[k] / maior
                    lista_sim.append(result)
                    break
                
        print(f'{int(lista[j])}/{int(lista[k])} = {int(lista_sim[j])}/{int(lista_sim[k])}')
return 0;
}

