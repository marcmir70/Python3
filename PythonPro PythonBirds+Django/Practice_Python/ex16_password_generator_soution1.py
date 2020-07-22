# Practice Python, Exercise 16 solution 1 - from 20140528 copied in 20190722
# - ref: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Exercise: a password generator. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# generate a password with length "passlen" with no duplicate characters in the password
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))  # MM: random.sample doesn't repeat elements!
print p