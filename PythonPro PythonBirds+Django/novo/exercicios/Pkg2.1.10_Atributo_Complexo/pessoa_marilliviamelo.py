# do Fórum Python Pro / Python Birds: Atributo Complexo
# baseado no código de marilliviamelo em 20190316_1947h
class Pessoa:
    def __init__(self, nome=None, idade = 35, *filhos ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo')
    #luciano = Pessoa(nome='Luciano', idade=49, renzo)
    #                                             ^
    # SyntaxError: positional argument follows keyword argument
    luciano = Pessoa('Luciano', 49, renzo) # no errors!
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(luciano.filhos)