print('* DEBUG: gerador novo_nome')

import random

def novo_nome():
    nomes=('Marcelo', 'Mellissa', 'Arthur', 'Priscilla')
    random_number = random.randint(0, len(nomes)-1)
    print('* DEBUG: gerador novo_nome > ', random_number)
    print('* DEBUG: gerador novo_nome > ', nomes[random_number])
    return nomes[random_number]

    # return choice(['Marcelo', 'Mellissa', 'Arthur', 'Priscilla'])
