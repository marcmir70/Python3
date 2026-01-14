#!/usr/bin/python3
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome; {}, Idade: {}'.format(*registro.strip().split(','))) # v4 try/finally
# except IndexError:
#     pass
finally:
    print('finally')
    arquivo.close()
    
if arquivo.closed:
    print('Arquivo já fechado!')