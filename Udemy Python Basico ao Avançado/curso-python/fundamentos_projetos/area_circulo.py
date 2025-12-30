#!/usr/bin/python3
from math import pi  # v15 optimized err msg
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print('É necessário informar o raio do círculo')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        help()
        sys.exit(errno.EPERM)   # code 1 ; not permitted operation
    
    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser um valor numérico' 
              + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)   # code 2 ; invalid argument
    
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo: ', area)
