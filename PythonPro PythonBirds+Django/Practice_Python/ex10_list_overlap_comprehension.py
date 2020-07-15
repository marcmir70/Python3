# Practice Python, Exercise 10 (similar to exercise 5) solution - from 20140410, done in 20190715
# - ref: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# Exercise: Take two lists and write a program that returns a list that contains only common elements
# between these lists (without duplicates). Make sure your program works on two lists of different sizes.
#           Write this in one line of Python using at least one list comprehension.
# concepts: List comprehensions; Random numbers, continued

a = [1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# result = [i for i in a if i in b]

result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print (result)