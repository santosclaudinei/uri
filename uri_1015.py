# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
# p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula,
# segundo a fórmula:
# distancia = √(x2-x1)² + (y2-y1)²

x1, y1 = input().split()
x2, y2 = input().split()
a = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** 0.5
print(f'{a:.4f}')
