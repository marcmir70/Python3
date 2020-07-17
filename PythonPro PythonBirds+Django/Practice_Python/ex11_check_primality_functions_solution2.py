# Practice Python, Exercise 11 solution 2 (without functions) - from 20140416, copied in 20190717
# - ref: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Exercise: Ask user a number and determine if it is prime or not. Use functions here!
#           Write this in one line of Python using at least one list comprehension.
# concepts: Functions, Reusable functions, Default arguments

import sys
number = input("Please enter a number" + "\n" + ">>>")
number = int(number)
prime = False #initiate boolean for true false, default false
if number > 0:
    for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
        if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
            continue
        elif number % x == 0: #If number is evenly divisible by x, it can't be prime
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.") #number wasn't evenly divisible by any x, so it's prime
elif number == 0:
    sys.exit("The number is not prime.") #According to the Google, 0 is not prime
else:#if number is less than 0, the number is not prime (according to the Google).
    sys.exit("The number is not prime.")