# Practice Python, Exercise 13 - from 20140430, done in 20190718
# - ref: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Exercise: ask user how many Fibonnaci numbers to generate and then generates them.
# concepts: Functions

from functions_base.ex13_fibonacci_numbers import fibonacci_numbers

fibonacci_numbers(int(input(f'How many Fibonacci number do you want?... ')))