#!/usr/bin/python3
def tag(tag, *args, **kwargs):  # solução do professor!
    if 'html_class' in kwargs:  # kwargs = argumentos nomeados
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v}" ' for k, v in kwargs.items())
    # ou a forma de acima ou esta: # attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'

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