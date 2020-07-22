# Practice Python, Exercise 15 - from 20140515, done in 20190721 by Marcelo Miranda github.com/marcmir70
# - ref: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Exercise: ask user a long string containing multiple words. Then, print it with the words in backwards order.

def words_reversal(texto):
    """ generates a text (string) with its words in reversal order
    Ex:

    >>> words_reversal('my name is Marcelo Miranda')
    Miranda Marcelo is name my

    :param texto: string
    :return: message
    """

    text_words_list = texto.split()
    text_words_reverted = []
    for i in range(len(text_words_list)):
        text_words_reverted.append(text_words_list[-(i+1)])

    print(' '.join(text_words_reverted))

    if __name__ == '__main__':
        words_reversal('my name is Marcelo Miranda')
