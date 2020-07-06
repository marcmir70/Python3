# Practice Python, Exercise 2 - from 20140205, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Exercise: Ask  user a number, and print out if it is even or odd
# Extras: 2. Ask user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

numb = input('Please type a number here > ')
numb = int(numb)
print(f" - let's call your number {numb} as \"num\".")
print()

check = input('Please type other number here > ')
check = int(check)
print(f" - let's call your number {check} as \"check\".")
print()

if numb % check == 0:
    print(f'{numb} is divisible by {check}!')
else:
    print(f"{numb} isn't divisible by {check}!")