class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {self.nome} -id:{id(self)}'

if __name__ == '__main__':
    mell = Pessoa(nome='Mell', idade=26)
    thu = Pessoa(nome='Thu', idade=21)
    marcelo = Pessoa(mell, thu, nome='Marcelo') # mell e thu filhos de marcelo
    print(Pessoa.cumprimentar(marcelo))
    print(id(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    print('filhos...')
    for filho in marcelo.filhos:
        print(f' - id:{id(filho)}, nome:{filho.nome}, {filho.idade} anos')
