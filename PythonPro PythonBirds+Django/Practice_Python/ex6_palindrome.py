# Practice Python, Exercise 6 - from 20140312, done in 20190707
# - ref: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Exercise: Ask the user for a string and print out whether this string is a palindrome or not.
#            (A palindrome is a string that reads the same forwards and backwards.)
# concepts: List indexing, Strings are lists

word_to_check = (input(f'Please inform a word... ').lower())

is_palindrome = True
for i in list(range(len(word_to_check))):
    if word_to_check[i] != word_to_check[-i-1]:
        print(f'{word_to_check} is not a palindrome!')
        is_palindrome = False
        break
if is_palindrome:
    print(f'{word_to_check} is a palindrome!')
