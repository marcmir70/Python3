#!/usr/bin/python3

# D. Polimorfismo
# Um mesmo nome de método, mas comportamentos diferentes dependendo do objeto
# Exemplo: 
#          
#          

class Animal:
    def __init__(self, nome):
        self.nome = nome

    # Método genérico na classe pai (Base)
    # Ele define QUE o animal fala, mas não COMO.
    # uma "promessa" (um método vazio)
    def falar(self):
        pass

class Cachorro(Animal):
    # Sobrescrita (Override) do método falar()
    # nas classes filhas ele se torna real e diferente.
    def falar(self):
        return f"{self.nome} diz: Au Au!"

class Gato(Animal):
    # Sobrescrita (Override) do método falar()
    def falar(self):
        return f"{self.nome} diz: Miau!"

# O POLIMORFISMO EM AÇÃO:
if __name__ == '__main__':
    # Criamos uma lista mista de animais
    meus_animais = [
        Cachorro("Rex"),
        Gato("Mingau"),
        Cachorro("Bob")
    ]

    print("Hora de ouvir os animais...\n")
    
    # O comando é o mesmo (falar()), mas o resultado varia 
    # de acordo com o objeto na lista.
    for animal in meus_animais:
        # Note que não perguntamos "if animal == Cachorro"
        # O Python sabe qual método chamar!
        print(animal.falar())
        