def contar_caracteres(palavra):
...     ordenada = sorted(set(palavra))
...     for caracteres in ordenada:
...         print(f'{caracteres}: {palavra.count(caracteres)}')