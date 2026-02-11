# criar classe Carro, e seus atributos e comportamentos
# acelerar : padrão=5, até no máximo de 180 (se a 178, poderá acelerar só 2)
# frear : no máximo, até 0, no máximo (se estiver a 3, poderá frear só 17)

if __name__ == '__main__':
    c1 = Carro(180)   # velocidade máxima
    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))