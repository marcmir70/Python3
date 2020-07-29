def conta_vogais(frase):
    espaço = " "
    vogais = ['a', 'e', 'i', 'o', 'u']
    print(f' qtide de espaços vazios: {frase.count(espaço)}')
    ordem = sorted(frase)
#    print(ordem) # debug na execução
    c_ant = ''
    for c in ordem:
        if (c in vogais) and (c != c_ant):
            print(f'{c}:{ordem.count(c)}')
            c_ant = c

#    for i in range(len(ordem)):
 #       if ordem[i] in vogais:
  #          print(f'{ordem[i]}= {frase.count(ordem[i])}')

# programa principal
f = str(input('digite um frase para contarmos vogais e espaços: '))
print(conta_vogais(f))