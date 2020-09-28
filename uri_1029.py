# Quase todo estudante de Ciência da Computação recebe em algum momento no início de seu curso de graduação
# algum problema envolvendo a sequência de Fibonacci. Tal sequência tem como os dois primeiros valores 0 (zero)
# e 1 (um) e cada próximo valor será sempre a soma dos dois valores imediatamente anteriores.
# Por definição, podemos apresentar a seguinte fórmula para encontrar qualquer número da sequência de Fibonacci:
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2);

# Uma das formas de encontrar o número de Fibonacci é através de chamadas recursivas. Isto é ilustrado a seguir,
# apresentando a árvore de derivação ao calcularmos o valor fib(4), ou seja o 5º valor desta sequência:

cont = 0

def fib (y):
    global cont
    if y == 1:
        cont += 1
        return 1
    elif y == 0:
        cont += 1
        return 0
    else:
        cont += 1
        return fib(y -1) + fib(y -2)

def main():   
    n = int(input())
    lista_fib = []

    for i in range(0, n):
            f = int(input())
            lista_fib.append(f)

    for j in range(0, len(lista_fib)):
            x = fib(lista_fib[j])
            print(f'fib ({lista_fib[j]}) = {cont - 1} calls = {x}')

main();
