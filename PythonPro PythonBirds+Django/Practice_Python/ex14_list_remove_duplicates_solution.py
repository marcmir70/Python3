# Practice Python, Exercise 14 - from 20140515, done in 20190721
# - ref: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Exercise: takes a list and return a new one that contains all elements of first one minus all duplicates.
# concepts: sets
# Extra 1.2 : using set ...

def list_duplicates_removal(lista):
    """ generate a set of common elements between two lists, without their duplicate ones
    Ex:
    >>> list_duplicates_removal([1, 2, 3, 4, 3, 2, 1])
    {1, 2, 3, 4}

    :param lista: list
    :return: list
    """

    print(list(set(lista)))