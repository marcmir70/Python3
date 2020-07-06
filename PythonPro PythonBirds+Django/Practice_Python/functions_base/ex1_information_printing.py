# Practice Python, Exercise 1 + extra - from 20140129, done in 20190702
def info_print(name, age, repeat_number):
    """ loop of printed text
    Ex:

    >>> info_print('miranda', 50, 3)
    1- Miranda will complete 100 years old in 2070.
    2- Miranda will complete 100 years old in 2070.
    3- Miranda will complete 100 years old in 2070.

    :param name: integer
    :param age: float
    :param repeat_number: integer
    :return: message
    """

    from datetime import date
    today = date.today()
    year_100th_age = today.timetuple().tm_year

    i = 1
    while i < repeat_number + 1:
        print(f'{i}- {name.title()} will complete 100 years old in'
              f' {year_100th_age + 100 - age}.')  # it did't need /n suggested on exercise
        i += 1

    if __name__ == '__main__':
        info_print('miranda', 50, 5)
