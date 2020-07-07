# Practice Python, Exercise 4 - from 20140226, done in 20190703
# - ref: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Exercise: asks the user for a number and then prints out a list of all the divisors of that number.
# Extra: variation to look for all divisors from the informed number and its previous ones till 2.
#      - this programs also identifies the number of divisors, and prime numbers!
#numbers_divisors #prime_numbers

initial_numb = int(input(f'Please inform me a number here > '))
numb = int(initial_numb)
print()

divisors = []
number_of_divisors = 0
prime_number = []
while numb >= 2:
    for i in list(range(numb,0,-1)):
        if numb % i == 0:
            number_of_divisors += 1
            divisors.append(i)
    if number_of_divisors == 2:
        print(f'{numb} is a prime number!')
        prime_number.append(numb)
    else:
        print(f'{numb} has {number_of_divisors} divisors: {divisors}')
    number_of_divisors = 0
    divisors = []
    numb -= 1
print()
print(f'The prime numbers between 2 and {initial_numb} are {len(prime_number)} listed below:')
print(prime_number)

