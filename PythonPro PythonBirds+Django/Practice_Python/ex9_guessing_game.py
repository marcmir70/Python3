# Practice Python, Exercise 9 - from 20140402, done in 20190714
# - ref: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Exercise: Generate a random number between 1 and 9 (including 1 and 9) and ask user
#           to guess it, then tell if he/she guessed too low, too high, or exactly right.
# concepts: Modules, Random numbers, User input

import random

random_number = random.randint(1, 9)

guess_number = int(input(f'Inform a number between 1 and 9 - including them - you want to guess... '))
 # for debug : print(f' -> you informed {guess_number} - an {type(guess_number)}')

if guess_number > random_number:
    print('  You guessed too high!')
    print(f'The random number I generated was {random_number}')
elif guess_number < random_number:
    print('  You guessed too low!')
    print(f'The random number I generated was {random_number}')
else:
    print('  You guessed exactly right!')