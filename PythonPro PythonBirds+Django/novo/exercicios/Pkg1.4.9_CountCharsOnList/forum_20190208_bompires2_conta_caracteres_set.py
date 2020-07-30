def contar_caracteres_set(s):
    """ Segunda opção de resolução do exercício de contagem de caracteres.
    Uma lista ordenada e contabilizada é armazenada em nova lista,
    depois transformada em set, que por fim é impresso em ordem.

    :param s: string a ser contada.
    """

    caracteres_ordenados = sorted(s)

    lista = []

    for c in caracteres_ordenados:
        lista.append(f'{c}: {caracteres_ordenados.count(c)}')

    lista_simples = set(lista)
    for s in sorted(lista_simples):
        print(s)

if __name__ == '__main__':
    contar_caracteres_lista('banana')
    print()
    contar_caracteres_set('banana')