#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v6.1 while w/ break , sequence in a row
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    for posicao, fib in enumerate(fibonacci(20)): # para listar os 20 primeiros números
        print(f'{posicao+1}: {fib}', end=',   ')
