#!/usr/bin/python3
class Potencia: # from master: /Udemy: 11 funcoes
    # calcula uma potência específica
    def __init__(self, expoente): # 'self' represents the current instance - Zen of Python: the explicit is better then implicit
        self.expoente = expoente # expoente = parameter for the constructor

    def __call__(self,base):
        return base ** self.expoente
    
if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)
    zenzicube = Potencia(6)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'5³ => {cubo(5)}')
        print(f'4⁴ => {Potencia(4)(2)}')
        print(f'7⁶ => {zenzicube(7)}')
        