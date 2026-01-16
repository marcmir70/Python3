# dicionario = {f'Item {i}': i*2 for i in range(10) if i%2==0}
dicionario = {i: i*2 for i in range(10) if i%2==0} # v5 dict comprehension
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')