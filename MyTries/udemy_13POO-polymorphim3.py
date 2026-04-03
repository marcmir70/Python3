#!/usr/bin/python3

# 149. Membros de Classe : os componentes da classe. 
# Atributos são as características (variáveis);  Métodos, as ações (funções).
# Exercicio: Crie uma classe Livro com atributos titulo e 
#            autor, e um método exibir_detalhes().

class Livro:
    # ATRIBUTO DE CLASSE (Compartilhado por todos os livros)
    # Membro de Classe: O dono é a fôrma (Classe). 
    # É uma informação que serve para todos, sem distinção.
    idioma = "Português"
    total_livros = 0

    def __init__(self, titulo, autor, paginas):
        # Membro de Instância (self): O dono é o objeto. 
        # Cada livro tem o seu título. 
        # Se eu mudar o título do Livro A, o Livro B continua igual.
        # ATRIBUTOS DE INSTÂNCIA (Cada livro tem o seu)
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        # Incrementando o contador da CLASSE
        Livro.total_livros += 1

    def exibir_detalhes(self):
        # Note que usamos 'self.idioma'. O Python busca na instância; 
        # se não achar, ele busca na Classe automaticamente!
        return f'O livro "{self.titulo}" (título em {self.idioma}) com {self.paginas} páginas é do(s) autor(es) {self.autor}'

if __name__ == '__main__':
    # 1. Criando instâncias (agora passando os argumentos corretos)
    livro1 = Livro("A ilha misteriosa", "Júlio Verne", 351)
    livro2 = Livro("Dom Casmurro", "Machado de Assis", 256)
    
    # 2. Mudando o idioma na CLASSE (afeta todos!)
    print(f"Total de livros: {Livro.total_livros}")
    print(livro1.exibir_detalhes()) # Note os parênteses () para executar o método!
    
    print("\n--- Mudando idioma da classe para Inglês ---")
    Livro.idioma = "Inglês"
    
    print(livro1.exibir_detalhes())
    print(livro2.exibir_detalhes())