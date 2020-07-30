# função para listar itens
# - ref.: https://www.youtube.com/watch?v=1TbOk_r3eYc : desempacotamento de parametros
def listar_itens(w, x, y, z):
    print(x, w, y, z)

lista = [21, 22, 67, 69]

# tentando listar os itens com o operador adequado:
listar_itens(*lista)