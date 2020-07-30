def contar_caracteres_lista(s):
    """    Primeira opção de resolução do exercício de contagem de caracteres.
    Uma lista ordenada é impressa item por item, desde que o item anterior não se repita.

    :param s: string a ser contada.
    """

    caracteres_ordenados = sorted(s)

    caracter = caracteres_ordenados[0]
    print(f'{caracter}: {caracteres_ordenados.count(caracter)}')
    cont_pass = 1

    for c in caracteres_ordenados:
        if c == caracter:
            pass
            cont_pass += 1
            print(f'passes: {cont_pass}')
        else:
            print('achei!')
            print(f'{c}: {caracteres_ordenados.count(c)}')
            caracter = c