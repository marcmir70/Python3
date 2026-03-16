#!/usr/bin/python3
# Encapsulamento: Esconder os detalhes internos de um objeto e proteger seus dados, 
#                 permitindo acesso apenas através de métodos específicos.
#    Exemplo: Você aperta o pedal do acelerador; você não precisa saber como a 
#             injeção eletrônica funciona por dentro.
#    Exercício: Crie uma classe ControleRemoto onde o volume só pode ser 
#             alterado por métodos aumentar e diminuir, nunca acessando 
#             o número do volume diretamente.

from random import randint

class ControleRemoto:
    def __init__(self, volume_inicial):
        self._volume = volume_inicial # atributo interno "protegido" pelo underline

    def consultar_volume(self): # método para LER o volume (Getter) mantendo-o privado
        if self._volume == 0:
            return "MUDO"
        return f"{self._volume} VU"

    def aumentar(self):
        if self._volume == 100:
            return f'(beep max) volume máximo alcançado!'
        self._volume += 1
        return f'(beep aum) +1 VU)'

    def diminuir(self):
        if self._volume == 0:
            return f'(beep min) volume mínimo alcançado!'
        self._volume -= 1
        return f'(beep dim) -1 VU)'

if __name__ == '__main__':
    # Instanciando objeto
    remoto = ControleRemoto(10)
    print(f'Volume real (interno): {remoto.consultar_volume()}')
    
    # Ações
    for i in range(1, 91+randint(0,4)):
        print(remoto.aumentar())
        print(f'Volume atual: {remoto.consultar_volume()}')
    for i in range(1, 103+randint(0,3)):
        print(remoto.diminuir())
        print(f'Volume atual: {remoto.consultar_volume()}')
