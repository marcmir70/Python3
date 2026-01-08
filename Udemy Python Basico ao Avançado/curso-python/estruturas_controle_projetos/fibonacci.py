#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v8 more changes
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(quantidade - 2):  # _ is for a not used variable
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(20): # para listar os 20 primeiros números
        print(fib)
