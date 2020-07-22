# Practice Python, Exercise 5 - from 20140320, Renzo's solution in 20190707 #justOneLineCode
# - ref: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Exercise: returns a list that contains only common elements between the informed lists - with different sizes.
# concepts: loops, conditionals, and any other programming constructs.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f'The common values are: {list(set(a).intersection(b))}')