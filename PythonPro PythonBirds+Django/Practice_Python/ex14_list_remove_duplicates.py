# Practice Python, Exercise 14 - from 20140515, done in 20190721
# - ref: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Exercise: takes a list and return a new one that contains all elements of first one minus all duplicates.
# concepts: sets

def list_duplicates_removal(lista):
    """ generate a set of common elements between two lists, without their duplicate ones
    Ex:
    >>> list_duplicates_removal([1, 1, 2, 3, 3, 3, 5, 8, 13, 21, 21, 21, 1, 21, 21, 55, 89, 3, 3, 89])
    [1, 2, 3, 5, 8, 13, 21, 55, 89]

    :param lista: list
    :return: list
    """
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)

    print(nova_lista)