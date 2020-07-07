# Practice Python, Exercise 3 - from 20140215, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Exercise: Take a list and write a program that prints out all its elements that are less than 5.
# concepts: Lists, More conditionals (if statements).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # example

for i in a:
    if i < 5:
        print(i)