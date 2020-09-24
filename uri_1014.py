# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km)
# e o total de combustível gasto (em litros).

distancia_total = int(input())
total_combustivel = float(input())
consumo = distancia_total / total_combustivel
print(f'{consumo:.3f} km/l')

