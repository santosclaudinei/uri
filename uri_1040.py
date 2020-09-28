# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal,
# correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1,
# respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem
# "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
# Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
# Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir
# a mensagem "Aluno em exame.".

# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
# Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. 
# Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
# e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) 
# ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 
# Para estes dois casos (aprovado ou reprovado após ter pego exame) 
# apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

def main():
    
    N1, N2, N3, N4 = input().split()
    
    N1  = float(N1)
    N2  = float(N2)
    N3  = float(N3)
    N4  = float(N4)
    if (0 <= N1 <= 10.0) and (0 <= N2 <= 10.0) and (0 <= N3 <= 10.0) and (0 <= N4 <= 10.0):
        media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

        print(f'Media: {media:.1F}')
    
        if media >= 7.0:
            print('Aluno aprovado.')
        elif 0 < media < 5.0:
            print('Aluno reprovado.')
        elif 5.0 <= media <= 6.9:
            print('Aluno em exame.')
            nota_exame = float(input())
            print(f'Nota do exame: {nota_exame}')
            resultado =  (media + nota_exame) / 2
            if resultado >= 5.0:
                print('Aluno aprovado.')
            else:
                print('Aluno reprovado.')
            print(f'Media final: {resultado:.1f}')  

main();

