# Practice Python, Exercise 8 - from 20140326, solution from site
# - ref: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Exercise: Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out congratulations to winner, ask if players want to start a new game)
# Rules: Rock beats scissors,  Scissors beats paper,  Paper beats rock
# concepts: While loops, Infinite loops, Break statements

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_))