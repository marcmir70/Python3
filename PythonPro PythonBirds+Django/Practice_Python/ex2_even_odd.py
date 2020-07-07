# Practice Python, Exercise 2 - from 20140205, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Exercise: Ask  user a number, and print out if it is even or odd
# concepts: Modular arithmetic (the modulus operator), Conditionals (if statements), Checking equality

numb = input('Please type a number here > ')
numb = int(numb)
print()

if numb % 2 == 0:
    print(f'{numb} is even.')
else:
    print(f'{numb} is odd.')