def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    Ex:

    >>> contar_caracteres('Marcelo')
    {'M': 1, 'a': 1, 'r': 1, 'c': 1, 'e': 1, 'l': 1, 'o': 1}
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        # contagem = resultado.get(caracter, 0)
        # contagem += 1
        # resultado[caracter] = contagem

        resultado[caracter] = resultado.get(caracter, 0) + 1 # # ou as três linhas acima em apenas uma

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('Marcelo'))
    print()
    print(contar_caracteres('banana'))
