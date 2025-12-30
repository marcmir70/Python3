#!/usr/bin/python3
from math import pi  # v8 function wo/ return

def circulo(raio):
    print('Area do círculo: ', pi * float(raio) ** 2)

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
