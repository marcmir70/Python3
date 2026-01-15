produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto: # or> chave in produto.keys()
    print(chave)

print('\n...\n')
for valor in produto.values():
    print(valor)

print('\n...\n')
for chave, valor in produto.items():
    print(chave, '=', valor)

