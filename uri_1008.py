# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
# o valor que recebe por hora e calcula o salário desse funcionário. A seguir,
# mostre o número e o salário do funcionário, com duas casas decimais.

NUMBER = int(input())
HORAS = int(input())
SALARY = float(input())
SALARY = SALARY * HORAS
print(f'NUMBER = {NUMBER}')
print(f'SALARY = U$ {SALARY:.2F}')
