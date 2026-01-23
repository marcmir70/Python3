#!/usr/bin/python3
bloco_atrs = ('bloco_accesskey', 'bloco_id') # lista de atributos suportados - aqui para tags de BLOCOS: span, div
ul_atrs = ('ul_id', 'ul_style') # aqui para tags de LISTA: ul

def filtrar_atrs(informados, suportados): # v5 named packing and unpacking
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)

def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    print(f'Atributos: {atributos}')
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>' # or use: filtrar_atrs(novos_atrs) replacing: atributos


def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))  # print(tag_bloco('inline e classe', 'info', True))  ## 'info e 'True' considerados como args
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True,conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'),classe='info'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', 
                    classe='info', inline=True)) # por agora ter parâmetros especisis, os demaais tem que ser nomeados
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info', 
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', ul_blabla='abc', ul_style='color:red'))