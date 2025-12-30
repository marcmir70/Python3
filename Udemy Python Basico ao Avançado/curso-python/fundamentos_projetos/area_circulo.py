#!/usr/bin/python3
from math import pi  # v10 getting arguments vis Terminal
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':   # print(sys.argv[1]) ## antes argv[0]
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo: ', area)
