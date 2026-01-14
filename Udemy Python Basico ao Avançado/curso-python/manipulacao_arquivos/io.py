#!/usr/bin/python3
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome; {}, Idade: {}'.format(*registro.split(','))) # v2 stream 1
arquivo.close
    
