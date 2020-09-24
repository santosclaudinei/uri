# Leia um valor inteiro, que é o tempo de duração em segundos 
# de um determinado evento em uma fábrica, e informe-o expresso
# no formato horas:minutos:segundos.

tempo = int(input())
hora = tempo // 3600
min = (tempo - (hora * 3600)) // 60
seg = (tempo - (hora * 3600) - (min * 60))
print(f'{hora}:{min}:{seg}')