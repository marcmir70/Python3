# Practice Python, Exercise 5 - from 20140320, done in 20190707
# - ref: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Exercise: returns a list that contains only common elements between the informed lists - with different sizes.
# Extra: 1. randomly generate two lists to test this

import random

a_size = 0
b_size = 0
while a_size == b_size:
    a_size = int(40 * random.random())
    b_size = int(40 * random.random())

a = []
b = []
for i in list(range(a_size)):
    a.append(int(50 * random.random()))
for i in list(range(a_size)):
    b.append(int(50 * random.random()))

print(a)
print(b)

c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(f'The common values are: {c}')