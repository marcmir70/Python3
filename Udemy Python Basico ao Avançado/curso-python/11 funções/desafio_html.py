#!/usr/bin/python3
def tag(tag, *args, **kwargs):
    pass

if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por'),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '), 
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert') 
    )

# resultado esperado:
# <p class="alert"><span >Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong>
#                  <span > e </span><strong id="ll">Leionardo Leitão</strong><span >.</span></p>