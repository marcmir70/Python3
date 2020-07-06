# Practice Python, Exercise 3 - from 20140215, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Exercise: Take a list and write a program that prints out all its elements that are less than 5.
# Extras: 1. Instead of printing the elements one by one, make a new list that has
# all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # example
lista = []
for i in a:
    if i < 5:
        lista.append(i)
print(lista)
print()

numb = input(f'Please type a number for me here > ')
numb = int(numb)
lista = []
for i in a:
    if i < numb:
        lista.append(i)
print(lista)

