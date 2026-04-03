#!/usr/bin/python3

# 149. Membros de Classe : os componentes da classe. 
# Atributos são as características (variáveis);  Métodos, as ações (funções).
# Exercicio: Crie uma classe Livro com atributos titulo e 
#            autor, e um método exibir_detalhes().

class Livro:
    # ATRIBUTO DE CLASSE (Compartilhado por todos os livros)
    # Membro de Classe: O dono é a fôrma (Classe). 
    # É uma informação que serve para todos, sem distinção.
    # idioma = "Português"
    total_livros = 0
    instituicao = "Biblioteca Nacional"

    def __init__(self, titulo, autor):
        # Membro de Instância (self): O dono é o objeto. 
        # Cada livro tem o seu título. 
        # Se eu mudar o título do Livro A, o Livro B continua igual.
        # ATRIBUTOS DE INSTÂNCIA (Cada livro tem o seu)
        self.titulo = titulo  # Instância
        self.autor = autor    # Instância
        # Mexemos no contador da CLASSE toda vez que um livro nasce
        Livro.total_livros += 1

    # MÉTODO DE INSTÂNCIA: Fala sobre UM livro específico
    def exibir_detalhes(self):
        # Note que usamos 'self.idioma'. O Python busca na instância; 
        # se não achar, ele busca na Classe automaticamente!
        return f'Livro "{self.titulo}" por {self.autor} (Local: {self.instituicao})'
    
    # MÉTODO DE CLASSE: Fala sobre a CLASSE (a fôrma)
    @classmethod
    def resetar_contador(cls):
        print(f"\n--- Resetando o contador da {cls.instituicao} ---")
        cls.total_livros = 0 # 'cls' aqui é o mesmo que 'Livro'


if __name__ == '__main__':
    # 1. Criando instâncias (agora passando os argumentos corretos)
    livro1 = Livro("A Ilha Misteriosa", "Júlio Verne")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")

    print(f"Livros criados: {Livro.total_livros}")
    
    # Chamamos o método de classe diretamente pela CLASSE, não pelo objeto
    Livro.resetar_contador()
    
    print(f"Livros criados após reset: {Livro.total_livros}")
