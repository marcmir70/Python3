palavra = 'paralelepipedo'

for letra in palavra:
    print(letra)

print('\n...\n')
for letra in palavra:
    print(letra, end=',') # the default is '\n'

print('\n...\n')
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
    
print('\n...\n')
for posicao, nome in enumerate(aprovados):
    print(posicao+1, nome)
    
print('\n...\n')
for posicao, nome in enumerate(aprovados):
    print(f'{posicao+1})', nome)
    
print('\n...\n')
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

print('\n...\n')
for letra in set('muito legal'):
    print(letra)

print('\n...\n')
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
