#!/usr/bin/python3
class Potencia:
    # calcula uma potência específica
    def __init__(self, expoente): # 'self' represents the current instance - Zen of Python: the explicit is better then implicit
        self.expoente = expoente # expoente = parameter for the constructor

    def __call__(self,base):
        return base ** self.expoente
    
if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'5³ => {cubo(5)}')
        print(Potencia(4)(2)) # f'4