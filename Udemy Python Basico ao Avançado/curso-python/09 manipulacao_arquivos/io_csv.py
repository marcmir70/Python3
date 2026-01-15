import csv

with open('pessoas.csv') as entrada: # CSV reader module
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
