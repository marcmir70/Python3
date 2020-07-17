# Practice Python, Exercise 11 solution 1 - from 20140416, copied in 20190716
# - ref: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Exercise: Ask user a number and determine if it is prime or not. Use functions here!
#           Write this in one line of Python using at least one list comprehension.
# concepts: Functions, Reusable functions, Default arguments

def get_number(prompt):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(prompt))


def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    # Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    # All other primes
    else:
        prime = True
        for check_number in range(2, (number / 2) + 1):
            if number % check_number == 0:
                prime = False
                break
    return prime


def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number, " is ", descriptor, "prime.", sep="", end="\n\n")


# never ending loop

while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctl-C to exit."))