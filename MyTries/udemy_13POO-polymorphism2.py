#!/usr/bin/python3

# D. Polimorfismo
# Um mesmo nome de método, mas comportamentos diferentes dependendo do objeto
# Exercicio: Crie uma lista com objetos Circulo e Quadrado. 
#            Ambos devem ter um método calcular_area().

from math import pi

class FormaGeometrica:
    def __init__(self, nome):
        self.nome = nome

    # Método genérico na classe pai (Base) - "promessa" (método vazio)
    def calcular_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__("Quadrado")
        self.lado = lado
    # Sobrescrita (Override) do método falar()
    # nas classes filhas se torna real e diferente.
    def calcular_area(self):
        return self.lado**2

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio
    # Sobrescrita (Override) do método falar()
    def calcular_area(self):
        return pi*self.raio**2

# O POLIMORFISMO EM AÇÃO:
if __name__ == '__main__':
    # lista mista de formas
    minhas_formas = [
        Quadrado(2),
        Quadrado(3),
        Circulo(3),
        Quadrado(4),
        Circulo(4),
        Circulo(5),
        Circulo(6),
        Quadrado(6)
    ]

    print("Hora de calcular a área das formas geométricas...\n")
    for forma in minhas_formas:
        area = forma.calcular_area()
        print(f'Forma: {forma.nome} | Área: {area:.2f}')
        