# criar classe Carro, seus atributos e comportamentos
# acelerar : padrão=5, até no máximo de 180 (se a 178, poderá acelerar só 2)
# frear : no máximo, até 0, no máximo (se estiver a 3, poderá frear só 17)
class Carro:
    def __init__(self, velocMax):
        self.velocMax = velocMax
        self.velocAtual = 0

    def acelerar(self, delta=5):
        max = self.velocMax
        new = self.velocAtual + delta
        self.velocAtual = new if new <= max else max
        return self.velocAtual

    def frear(self, delta):
        new = self.velocAtual - delta
        self.velocAtual = new if new >= 0 else 0
        return self.velocAtual

if __name__ == '__main__':
    c1 = Carro(180)
    for _ in range(25):
        print(c1.acelerar(8))

    print('...')

    for _ in range(10):
        print(c1.frear(delta=20))