# for i in range(1,10):
#     print(i)
# else:
#     print('Fim!')

from random import randint

def sortear_dado():
    return randint(1, 6)

acertos = 0
tentativas = 0

while True:
    tentativas += 1

    for i in range(1,7):
        if i % 2 == 1:
            continue

        if sortear_dado() == i:
            print('ACERTOU', i, '- acertos até agora:', acertos)
            acertos += 1
    #        break
    else:
        print('Não acertou o número - tentativas até agora:', tentativas)

    print(f'* Percentual de acertos até o momento: {100*acertos/tentativas}%')
