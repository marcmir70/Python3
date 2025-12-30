#!/usr/bin/python3
from math import pi  # v13 leaving w/ err
import sys
import errno


def help():
    print('É necessário informar o raio do círculo')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        help()
        sys.exit(errno.EPERM)   # code 1 ; not permitted operation ## sys.exit(1)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo: ', area)
