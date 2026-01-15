#!/usr/bin/python3
# desafio : Extrair o 9. e 4. campos do arquivo CSV sobre Região de influência das Cidades do IBGE, 
# que pode ser baixado em:  http://www.geoservicos.ibge.gov.br/geoserver/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=CGEO:RedeUrbanaSintese_Regic2007&outputFormat=CSV 
# ignorando a primeira linha que é o cabeçalho - arquivo ISO-8859-1 (aka latin1)

import csv
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print(TerminalColor.ERRO + 'É necessário informar o nome do arquivo CSV a ser processado')
    print('Exemplo: {} desafio-ibge.csv'.format(sys.argv[0][2:]) + TerminalColor.NORMAL)


def read(arquivo):
    i=1
    with open(arquivo, encoding='ISO-8859-1') as entrada: # CSV reader module
        for pessoa in csv.reader(entrada):
            if i > 1:
                print('{} , {}'.format(pessoa[8], pessoa[3]))
                # print('linha {}: {} , {}'.format(i, pessoa[8], pessoa[3]))
            i += 1
            # if i > 5: # para validar que primeira linha não foi lida!
            #     break


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        help()
        sys.exit(errno.EPERM)   # code 1 ; not permitted operation
    
    import sys
    read(sys.argv[1])
    