#!/usr/bin/python3
def log(function):
    def decorator(*args, **kwargs):
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator

@log
# @ log # se comentar, log não é chamado
def soma(x,y):
    return x + y

@log
def sub(x,y):
    return x - y

if __name__ == '__main__':
    print(soma(5,7))
    # soma(5,7) # sem o print, só chama log
    print(sub(5, y=7))


# # exemplo inicial...
# def soma(a,b):
#     def soma_c(c): # inner function
#         return a + b + c
#     return soma_c

# soma_5 = soma(2,3)
# print(soma_5(5))
# print(soma_5(50))
# print(soma(1,3)(5))
# print(soma(1,3,5))