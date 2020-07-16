# Practice Python, Exercise 11 - from 20140416, done in 20190716
# - ref: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Exercise: Ask user a number and determine if it is prime or not. Use functions here!
#           Write this in one line of Python using at least one list comprehension.
# concepts: Functions, Reusable functions, Default arguments

def check_prime(number):
    number_of_divisors = 0
    for i in list(range(number, 0, -1)):
        if number % i == 0:
            number_of_divisors += 1
    if number_of_divisors == 2:
        return(f'{number} is a prime number!')
    else:
        return (f'{number} is not a prime number!')

number = int(input(f'Please say me an integer number to check if it is prime... '))
print(check_prime(number))