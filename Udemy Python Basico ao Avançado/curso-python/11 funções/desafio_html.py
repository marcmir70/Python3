#!/usr/bin/python3
def conteudo(params):               ### primeira solução de Marcelo Miranda
    dados = ''                      # linhas de debug (aqui e abaixo): # print(f'type(params): {type(params)}')
    if type(params) is tuple:       # print('aqui') # quando params vem de *args é tipo TUPLE; 
        for texto in params:        # print(f'texto: {texto}')
            dados += texto          # print(f'dados: {dados}')
    elif type(params) is dict:      # quando params vem de kwargs é tipo DICT
        dados = ' '.join(f'{chave.split("_")[-1]}="{valor}"'
            for chave, valor in params.items())     # print(f'dados: {dados}')
    return dados

def tag(tag, *args, **kwargs): # args: conteúdo; kwargs: propriedades da tag
                            # Debug... print(f'args: {args} / kwargs: {kwargs}')
    if len(kwargs)== 0:
        if len(args) == 0:
            return 'no content'                                      # error!?
        elif len(args) > 0:
            return f'<{tag}>{conteudo(args)}</{tag}>'
    elif len(kwargs) > 0:
        if len(args) == 0:
            return f'<{tag} {conteudo(kwargs)}>no content</{tag}>'  # error!?
        elif len(args) > 0:
            return f'<{tag} {conteudo(kwargs)}>{conteudo(args)}</{tag}>'

if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por'),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '), 
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert') # , end='' # (não fez efeito) pra pôr tudo junto
    )

# resultado esperado:
# <p class="alert"><span >Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong>
# <span > e </span><strong id="ll">Leionardo Leitão</strong><span >.</span></p>