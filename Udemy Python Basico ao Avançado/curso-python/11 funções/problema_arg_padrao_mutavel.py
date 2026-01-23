#!/usr/bin/python3
# def fibonacci(sequencia=[0,1]): # lista é algo mutável!
def fibonacci(sequencia=(0,1)): # agora tupla!
     # uso de mutáveis como valor default (armadilha)
        #  sequencia.append(sequencia[-1] + sequencia[-2])
        #  return sequencia
    return sequencia + (sequencia[-1] + sequencia[-2],)

if __name__ == '__main__':
     inicio = fibonacci()
     print(inicio, id(inicio))
     print(fibonacci(inicio))
     restart=fibonacci()
     print(restart, id(restart))