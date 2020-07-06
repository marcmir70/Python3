# Practice Python, Exercise 3 - from 20140226, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Exercise: asks the user for a number and then prints out a list of all the divisors of that number.

numb = input(f'Please inform me a number here > ')
numb = int(numb)
print()

divisors = []
for i in list(range(numb,0,-1)):
    if numb % i == 0:
        divisors.append(i)

print(f'These/This are the divisors of {numb} : {divisors}')