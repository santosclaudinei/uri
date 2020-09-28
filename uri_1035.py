# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A,
# e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A
# for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

dados = input().split()
A, B, C, D = dados

if((int(B) > int(C)) and (int(D) > int(A))):
    if((int(C) + int(D)) > (int(A) + int(B))):
        if((int(C) > 0) or (int(D) > 0)):
            print("Valores aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")