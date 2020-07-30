"Módulo que contém operações Matemáticas"

def soma(parcela, parcela_2):
    """Essa função calcula a soma de duas parcelas

    :param parcela: number
    :param parcela_2: number
    :return: number
    """
    return parcela + parcela_2

# print(__name__) # "dunder name" <- truque para identificar o módulo
# evitar que o código de teste de um módulo seja executado
# quando dentro de outros módulos
if __name__=='__main__':
    # testando a função soma
    print(soma(1,2)) # imprimindo
