def conta_vogais(frase):
    espaço = " "
    lista_vogais = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    print(f'qtide de espaços vazios: {frase.count(espaço)}')    # retirado \n no print acima

    # for vogal in frase:                                       # linha errada
    ordem = sorted(frase)                                       # acrescentada esta linha
    print(ordem)                                                # acrescentada esta linha

    for vogal in ordem:
        if vogal in vogais:
            lista_vogais.append(vogal)
            qtide = ({x:lista_vogais.count(x) for x in lista_vogais})   # cria dicionário de espaços e vogais com a quantidade de cada um
            print(f'qtide de vogais:')
    for k, v in qtide.items():
        print(f'{k}: {v}')

# acrescentada estas linhas abaixo
f = str(input('digite frase para contarmos vogais e espaços: '))
print(conta_vogais(f))