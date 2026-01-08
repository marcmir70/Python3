#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v5 challenge: using SUM function
def fibonacci(limite):
    resultado = [0, 1]
    while resultado [-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
