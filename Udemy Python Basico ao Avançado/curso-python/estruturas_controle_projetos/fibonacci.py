#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v7 FOR w/ RANGE (less loc -lines of code)
def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(20): # para listar os 20 primeiros números
        print(fib)
