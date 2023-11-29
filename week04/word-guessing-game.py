# Added a list of words in a separate file which is then used to randomly select a secret word.

import random

print('Welcome to the word guessing game!')

secret_word_list =[]

with open("week04\secret-words.txt") as secret_words:
    for line in secret_words:
        line = line.strip()
        secret_word_list.append(line)

guess_attempts = 1

user_guess = ''

play_again = 'Yes'

length_user_guess = len(user_guess)

while play_again.upper() == 'YES':
    secret_word = secret_word_list[random.randrange(0 , 7)]
    length_secret_word = len(secret_word)
    print('Your hint is:', end='')
    for letter in secret_word:
        print('_ ', end='')
    print()
    while user_guess.upper() != secret_word.upper():
        if length_user_guess != length_secret_word:
            print('Your guess must be the same length as the hint.')
            guess_attempts += 1
            user_guess = input('What is your guess?')
            length_user_guess = len(user_guess)
        else:
            for letter, char in zip(user_guess, secret_word):
                if letter == char:
                    print(char.upper(), end='')
                elif secret_word.__contains__(letter):
                    print(letter.lower(), end='')
                else:
                    print('_ ', end='')
            guess_attempts += 1
            user_guess = input(' What is your guess?').upper()
            length_user_guess = len(user_guess)
    print(f'Congratulations you guessed it!\nIt took you {guess_attempts} tries.')
    guess_attempts = 0
    play_again = input('Do you want to play again?')