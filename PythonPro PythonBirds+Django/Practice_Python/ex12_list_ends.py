# Practice Python, Exercise 12 - from 20140425, done in 20190717
# - ref: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Exercise: Write a program that takes a list of numbers and makes a new one of only first
# and last elements of the given list. For practice, write this code inside a function.
# concepts: Lists and properties of lists, List comprehensions (maybe), Functions

def list_first_last (list1):
    list2 = []
    list2.append(list1[0])
    list2.append(list1[len(list1)-1])
    return list2

a = [5, 10, 15, 20, 25]
print(f'initial list: {a}')
print(f'new list: {list_first_last(a)}')