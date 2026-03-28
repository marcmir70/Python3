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

    def __str__(self):
        return f"Forma: {self.nome:14} de {self.medidas()} => {self.calcular_area()}"

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__("Quadrado")
        self.lado = lado

    def medidas(self):
        return f'Lado = {self.lado:<4}'
    
    # Sobrescrita (Override) do método falar()
    # nas classes filhas se torna real e diferente.
    def calcular_area(self):
        return f'Área = Lado² = {self.lado**2:>6.2f}'

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio

    def medidas(self):
        return f'Raio = {self.raio:<4}'
    
    # Sobrescrita (Override) do método falar()
    def calcular_area(self):
        return f'Área = π · Raio² = {pi*self.raio**2:6.2f}'

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.base = base
        self.altura = altura

    def medidas(self):
        return f'Lado = {self.base}, Altura = {self.altura}'
    
    # Sobrescrita (Override) do método falar()
    def calcular_area(self):
        return f'Área = Base · Altura / 2 = {self.base*self.altura/2:6.2f}'

# O POLIMORFISMO EM AÇÃO:
if __name__ == '__main__':
    # lista mista de formas
    minhas_formas = [
        Quadrado(2),
        Circulo(1),
        Triangulo(2,4),
        Quadrado(3),
        Circulo(1.5),
        Triangulo(3,3),
        Quadrado(4),
        Circulo(2),
        Circulo(2.5),
        Circulo(3)
    ]

    print("Hora de calcular a área das formas geométricas...\n")
    for forma in minhas_formas:
        print(forma)
        