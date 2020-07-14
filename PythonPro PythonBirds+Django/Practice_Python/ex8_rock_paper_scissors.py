# Practice Python, Exercise 8 - from 20140326, done in 20190713
# - ref: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Exercise: Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out congratulations to winner, ask if players want to start a new game)
# Rules: Rock beats scissors,  Scissors beats paper,  Paper beats rock
# concepts: While loops, Infinite loops, Break statements

user_name = []
for i in list(range(2)):
    user_name.append(input(f'Player {i+1}, please inform your name... '))

new_game = True
while new_game:
    user_play = []
    for i in list(range(2)):
        valid_option = False
        while not valid_option:
            option = input(f'{user_name[i].upper()}, please say "Rock", "Paper" ou "Scissors"... ').lower()
            if option != 'rock' and option != 'paper' and option != 'scissors':
                print(f'Invalid input = {option}! You have not entered rock, paper or scissors. Please try again.')
            else:
                valid_option = True
                user_play.append(option)
    if user_play[0] == user_play[1]:
        print('It is a tie!')
    elif (( user_play[0] == 'rock' and user_play[1] == 'scissors' ) or
        ( user_play[0] == 'scissors' and user_play[1] == 'paper' ) or
        ( user_play[0] == 'paper' and user_play[1] == 'rock' )):
            print(f'Congratulations, {user_name[0]}! You win!')
    else:
        print(f'Congratulations, {user_name[1]}! You win!')
    answer = ''
    while answer == '' or ( answer[0].upper() != 'Y' and answer[0].upper() != 'N' ):
        answer = input(f'Do you want to play again?... ')
        if ( answer[0].upper() != 'Y' and answer[0].upper() != 'N' ):
            print(f'** Error! Please inform Y, Yes, N, or No! **')
    if answer[0].upper() == 'N':
        new_game = False
print()
print('Thanks for playing!')