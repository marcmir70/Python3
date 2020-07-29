def count_vowels_and_space(text: str) -> dict:
    dct = {' ': 0,'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in dct:
        dct[char] = text.count(char)
    return dct

f = str(input('digite frase para contar vogais e espaços: '))
print(count_vowels_and_space(f))