from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome

def main():
    while True:
        nome = novo_nome() # retorna uma string a cada vez que executar
        if not nome_existe(nome): # pode sempre retornar False
            add_nome(nome) # não precisa fazer nada / pode ser bloco vazio
            break

    print(f'Criado novo nome de testes: "{nome}"')

if __name__ == '__main__':
main()