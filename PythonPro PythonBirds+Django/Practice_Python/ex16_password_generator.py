# Practice Python, Exercise 16 - from 20140528, done in 20190722 by Marcelo Miranda
# - ref: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Exercise: a password generator. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Extra: Ask user how strong they want his/her password. For weak passwords, pick a word or two from a list.

import string
import random

def pw_gen(size = 8, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    # it is not good to use string.printable and string.whitespace constants (above)!
	return ''.join(random.choice(chars) for _ in range(size)) # MM: random.choice can repeat elements!

print('How many characters do you want in your password? ')

min_chars = 8
ok = False

while not ok:
    num_chars = int(input('Type here > '))
    if num_chars >= min_chars:
        ok = True
    else:
        print(f'Error! A password with {num_chars} is too weak! Try again... ')

print(f'Here it is the {num_chars}-chars password created: \n{pw_gen(num_chars)}')
