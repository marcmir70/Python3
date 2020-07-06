# Practice Python, Exercise 1 + extra - from 20140129, done in 20190702
# - ref: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Exercise: asks the user his/her name and age,
#           print out message to him/her that telling the year they will turn 100 years old.
# Extras:   asking user other number and print out many copies of the previous message on separate lines
from Practice_Python.functions_name import info_print

name = input("Give me your name, please... ")
age = int(input("Also let me know your age... "))
numb = input(f'For last, {name.title()}, inform any number... ') # Title name - first letter in upper case

print()
print(" - You informed the number " + numb)
numb = int(numb)
print()

info_print(name, age, numb)