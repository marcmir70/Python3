# Practice Python, Exercise 12 solution - from 20140425, copied in 20190717
# - ref: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Exercise: Write a program that takes a list of numbers and makes a new one of only first
# and last elements of the given list. For practice, write this code inside a function.
# concepts: Lists and properties of lists, List comprehensions (maybe), Functions

def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

a = [5, 10, 15, 20, 25]
print(f'initial list: {a}')
print(f'new list: {list_ends(a)}')