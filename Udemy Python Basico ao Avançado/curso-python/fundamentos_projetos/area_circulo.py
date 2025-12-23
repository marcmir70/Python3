# v2
# -*- coding: utf-8 -*-
from string import Template

pi = 3.14 # quando estava 3,14 repetia diversas vezes este valor (como string)
raio = 15
area = pi * (raio ** 2)

msg = Template ('A área do círculo de raio $R é $A')

print (msg.substitute(R=raio, A=area))

# print (f'A área do círculo de raio {raio} é {area}')
