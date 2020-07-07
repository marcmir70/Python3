# Practice Python, Exercise 5 - from 20140320, done in 20190707
# - ref: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Exercise: returns a list that contains only common elements between the informed lists - with different sizes.
# Extra: 2. Write this in one line of Python!

## I didn't find the solution yet!

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(f'The common values are: {c}')

