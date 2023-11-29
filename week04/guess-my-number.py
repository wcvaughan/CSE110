import random

# random_num = random.randint(1, 12)

play_again = 'yes'

while play_again.upper() == 'YES':
    magic_num = random.randint(1, 100)

    user_guess = -1

    guess_attempts = 0

    while user_guess != magic_num:
        user_guess = int(input('What is your guess?'))

        if user_guess > magic_num:
            print('lower')
            guess_attempts += 1
        elif user_guess < magic_num:
            print('higher')
            guess_attempts += 1
        else:
            print('You guessed it!')
            print(f'You had:{guess_attempts} number of guesses.')

    play_again = input('Do you want to play again?')


