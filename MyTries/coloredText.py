#!/usr/bin/python3
import sys
import errno
from random import randint


textColor = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', 
             '\033[95m', '\033[96m', '\033[97m', '\033[0m']
    #        RED       , GREEN     , YELLOW    , BLUE      ,
    #        PURPLE    , CYAN      , WHITE     , END
    # DARKCYAN = '\033[36m'


class TextFormat:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'


def help():
    print(textColor[0] + 'É necessário informar um texto')
    print('Sintaxe: {} <texto> [separador]'.format(sys.argv[0][2:]))
    print('         onde <texto> é obrigatório e [separador] é opcional' + 
          textColor[7])


def colored(text):
    for letra in text:
        aleat = randint(0, len(textColor) - 1)
        print(textColor[aleat] + letra , end = sys.argv[2] + textColor[aleat])


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        help()
        sys.exit(errno.EPERM)   # code 1 ; not permitted operation
    
#        sys.exit(errno.EINVAL)   # code 2 ; invalid argument

    text = sys.argv[1]
    colored(text)

