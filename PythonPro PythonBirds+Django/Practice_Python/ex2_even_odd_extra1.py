# Practice Python, Exercise 2 - from 20140205, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Exercise: Ask  user a number, and print out if it is even or odd
# Extra: 1. If the number is a multiple of 4, print out a different message.

numb = input('Please type a number here > ')
numb = int(numb)
print()

if numb % 4 == 0:
    print(f'{numb} is divisible by 4.')
elif numb % 2 == 0:
    print(f'{numb} is even.')
else:
    print(f'{numb} is odd.')