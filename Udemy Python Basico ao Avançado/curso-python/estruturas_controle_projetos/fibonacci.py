#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, ... ## v2.1 improvement: to really stop after the limit is reached
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while penultimo + ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo

if __name__ == '__main__':
    fibonacci(6766)
