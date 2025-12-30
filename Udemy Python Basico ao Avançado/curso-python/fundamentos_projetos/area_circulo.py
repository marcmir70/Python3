#!/usr/bin/python3
from math import pi  # v6 - a bit about module

raio = input('Informe o raio: ')
print ('Área do círculo:', pi * float(raio) ** 2)

print('nome do módulo ', __name__)    # on VS Code returns __main__ ; on Python via import, area_circulo
print('nome do pacote ', __package__) # on VS Code returns None
