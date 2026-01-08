#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v6 while w/ break
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(20): # para listar os 20 primeiros números
        print(fib)
