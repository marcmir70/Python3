# Practice Python, Exercise 9 - from 20140402, done in 20190714
# - ref: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Exercise: Generate a random number between 1 and 9 (including 1 and 9) and ask user
#           to guess it, then tell if he/she guessed too low, too high, or exactly right.
# concepts: Modules, Random numbers, User input

import random

random_number = random.randint(1, 9)
guess = 0
count = 0

while guess != random_number and guess != 'exit':
    guess = input(f'Inform a number between 1 and 9 - including them - you want to guess, or type "exit" to stop... ')

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess > random_number:
        print('  You guessed too high!')
    elif guess < random_number:
        print('  You guessed too low!')
    else:
        if count > 1:
            print(f'  You guessed exactly right! And you took {count} tries!')
        else:
            print(f'  You guessed exactly right! And you took it in your 1st try! Wow!!')