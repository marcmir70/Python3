# Practice Python, Exercise 13 - from 20140430, done in 20190718
def fibonacci_numbers(count):
    """ generate a quantity of Fibonacci numbers
    Ex:

    >>> fibonacci_numbers(0)
    []
    >>> fibonacci_numbers(1)
    [1]
    >>> fibonacci_numbers(2)
    [1, 1]
    >>> fibonacci_numbers(7)
    [1, 1, 2, 3, 5, 8, 13]

    :param quantity: integer
    :return: list
    """

    a = 0
    b = 1
    aux = 0
    numbers = []
    for i in range(0, count, 1):
        numbers.append(b)
        aux = a
        a = b
        b = aux + b
    print(numbers)

    if __name__ == '__main__':
        fibonacci_numbers(0)
        fibonacci_numbers(1)
        fibonacci_numbers(2)
        fibonacci_numbers(7)