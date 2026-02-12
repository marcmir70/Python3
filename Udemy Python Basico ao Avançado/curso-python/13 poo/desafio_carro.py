# criar classe Carro, e seus atributos e comportamentos
# acelerar : padrão=5, até no máximo de 180 (se a 178, poderá acelerar só 2)
# frear : no máximo, até 0, no máximo (se estiver a 3, poderá frear só 17)
veloc = 0

class Carro:
    def __init__(self, maxVeloc):
        self.maxVeloc = maxVeloc

    def acelerar(self, delta=5):
        global veloc
        if veloc + delta > self.maxVeloc:
            veloc = self.maxVeloc
        else:
            veloc += delta
        return veloc

    def frear(self, delta):
        global veloc 
        self.delta = delta
        if veloc - self.delta < 0:
            veloc = 0
        else:
            veloc -= delta
        return veloc

if __name__ == '__main__':

    c1 = Carro(180)   # velocidade máxima
    for a in range(25):
        print(c1.acelerar(8))
    
    print('...')

    for f in range(10):
        print(c1.frear(delta=20))