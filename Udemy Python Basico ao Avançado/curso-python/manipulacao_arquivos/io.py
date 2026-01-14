#!/usr/bin/python3
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome; {}, Idade: {}'.format(*registro.strip().split(','))) # v3 stream 2
arquivo.close
    
