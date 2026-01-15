#!/usr/bin/python3
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida: # v6 writing a file f/ a CSV one
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome; {}, Idade: {}'.format(*pessoa), file = saida) # v5 with

if arquivo.closed:
    print('Arquivo já fechado!')

if saida.closed:
    print('Arquivo de saída já fechado!')