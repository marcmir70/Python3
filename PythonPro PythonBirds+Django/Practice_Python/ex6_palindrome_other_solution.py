# Practice Python, Exercise 6 - from 20140312, done in 20190707
# - ref: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Exercise: Ask the user for a string and print out whether this string is a palindrome or not.
#            (A palindrome is a string that reads the same forwards and backwards.)
# concepts: List indexing, Strings are lists

wrd=input("Please enter a word... ")
wrd=str(wrd)
rvs=wrd[::-1]

if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")