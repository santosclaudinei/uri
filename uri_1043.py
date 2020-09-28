# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

# Perimetro = XX.X

# Em caso negativo, calcule a área do trapézio que tem A e B
# como base e C como altura, mostrando a mensagem

# Area = XX.X

def main():

    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

    if(A - B) < C and (A + B) > C:
        if(A - C) < B and (A + C) > B:
            if(B - C) < A and (B + C) > A:
                print(f'Perimetro = {A + B + C:.1f}')
    else:
        print(f'Area = {((A * C)/2) + ((B * C)/2):.1f}')

main();