# Practice Python, Exercise 7 - from 20140319, done in 20190713
# - ref: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# Exercise: Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# concepts: List comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

c = []
for i in a:
    if i % 2 == 0:
        c.append(i)
print(c)