def executar(funcao):  # class 125 (section 11 functions) abbout 'callable'
    if callable(funcao):
        funcao()
    else:
        print(f"function '{funcao} is not 'callable'")

def bom_dia():
    print('Bom dia!')

def boa_tarde():
    print('Boa tarde!')

if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1) # retornaria TypeError: 'int' object is not callable