def executar(funcao):
    if callable(funcao): # class 125
        funcao()

def bom_dia():
    print('Bom dia!')

def boa_tarde():
    print('Boa tarde!')

if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1) # retornaria TypeError: 'int' object is not callable