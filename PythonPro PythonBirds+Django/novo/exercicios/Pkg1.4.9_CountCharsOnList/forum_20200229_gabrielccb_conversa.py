def conversao (s):
    ordem_frase = sorted(s)
    length = len(ordem_frase)
    print ("O tamanho total do texto é: ", length, "\n")
    selected_letter = ordem_frase[0]
    counter = 1

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    vowel_counter = 0
    consonants_counter = 0
    space_counter = 0

    for ll in ordem_frase[1:]:
        if ll == selected_letter:
            counter += 1
        else:
            print(f'{selected_letter}: {counter}')
            if selected_letter in vowels:
                vowel_counter += counter
            elif selected_letter in consonants:
                consonants_counter += counter
            else:
                space_counter += counter
            counter = 1
            selected_letter = ll

    print(f'{selected_letter}: {counter}')

    if selected_letter in vowels:
        vowel_counter += counter
    elif selected_letter in consonants:
        consonants_counter += counter
    else:
        space_counter += counter

    print("Total de vogais no texto: ", vowel_counter)
    print("Total de consoantes no texto: ", consonants_counter)
    print("Total de espaços no texto: ", space_counter)

if __name__ == '__main__':
    dd = input('Insira uma frase: ')
    dd = dd.lower()
    resul = conversao(dd)