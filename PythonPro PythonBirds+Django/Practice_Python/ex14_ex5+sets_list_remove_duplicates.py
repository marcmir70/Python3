# Practice Python, Exercise 14 - from 20140515, done in 20190721
# - ref: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Exercise: takes a list and return a new one that contains all elements of first one minus all duplicates.
# concepts: sets
# Extra 2: do Exercise 5 using sets

def list_duplicates_removal(list1,list2):
    """ generate a set of common elements between two lists, without their duplicate ones
    Ex:
    >>> list_duplicates_removal([1, 1, 2, 3, 5, 8, 13, 21, 55, 89], [1, 2, 3, 3, 5, 6, 8, 9, 10, 12, 13])
    {1, 2, 3, 5, 8, 13}

    :param list1: list
    :param list2: list
    :return: set
    """
    common_elements = set()
    for i in list1:
        for j in list2:
            if i == j:
                common_elements.add(i)

    print(common_elements)