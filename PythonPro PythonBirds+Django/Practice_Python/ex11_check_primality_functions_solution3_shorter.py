# Practice Python, Exercise 11 solution 3 (without functions) - from 20140416, copied in 20190717
# - ref: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Exercise: Ask user a number and determine if it is prime or not. Use functions here!
#           Write this in one line of Python using at least one list comprehension.
# concepts: Functions, Reusable functions, Default arguments

# Assumes that "a" contains an integer > 2 whose primality needs to be verified
# The algorithm builds a list of factors including the number 2 and all odd numbers
# up to the square root of "a", and then checks if any of those numbers divides "a"
# without a remainder - if so then "a" is not prime, else it is
import math
a = int(input('Type a number... '))
if sum([ True if a%factor == 0 else False for factor in ( [2] + list(range(3,int(math.sqrt(a)),2) )) ]):
  print("Number is composite")
else:
  print("Number is prime")