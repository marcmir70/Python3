# Practice Python, Exercise 1 - from 20140129, done in 20190701
# - ref: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Exercise: asks the user his/her name and age,
#           print out message to him/her that telling the year they will turn 100 years old.
# concepts: Getting user input, Manipulating strings (a few ways)

name = input("Give me your name, please... ")
age = int(input("Also let me know your age... "))

print()

from datetime import date
today = date.today()
year_100th_age = today.timetuple().tm_year

print(f' - {name.title()} will complete 100 years old in '
      f'{year_100th_age + 100 - age}.')  # it did't need /n suggested on exercise

print()