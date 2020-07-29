# empacotando itens
# - ref.: https://www.youtube.com/watch?v=1TbOk_r3eYc : 5:45 empacotamento de parametros
def somar(*args):
    soma = 0
    for i in range(0, len(args)):
        soma += args[i]
    return soma

# testando
print(somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(somar(77, 23))