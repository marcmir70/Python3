#!/usr/bin/python3

# C. Herança
# Herança: Criar novas classes a partir de classes existentes, aproveitando 
#          atributos e métodos.
# Exemplo: Uma classe Animal tem o método comer(). 
#          A classe Cachorro herda de Animal e ganha comer() automaticamente, 
#          mas adiciona o latir().
# Exercício: Pense em uma classe Veiculo. 
#            Crie uma subclasse Moto que herde de Veiculo.

class Veiculo: # Superclasse (Classe Pai)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        return f'Veículo ligado!'

    def acelerar(self):
        pass

    def frear(self):
        pass

class Moto(Veiculo): # Subclasse (Classe Filha)
# Indicamos a herança colocando a classe pai entre parênteses
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo) # super() chama __init_ do Veiculo para tratar marca e modelo
        self.cilindradas = cilindradas

    def estacionar(self):
        pass

    def empinar(self):
        return f'A {self.modelo} de {self.cilindradas}cc está empinando!'

if __name__ == '__main__':
    # Criamos uma moto
    moto = Moto("Honda", "CG", 250)

    print(moto.ligar()) # método ligar() da classe Veiculo (Herança)

    print(moto.empinar()) # método empinar() específico da classe Moto
    
    print(moto.acelerar()) # método acelerar() da classe Veiculo (Herança)
    
    print(moto.estacionar()) # método estacionar() específico da classe Moto