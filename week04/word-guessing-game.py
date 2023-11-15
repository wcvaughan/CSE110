print('Welcome to the word guessing game!')

secret_word = 'HORIZON'

secret_word_list = list(secret_word.strip(""))

length_secret_word = len(secret_word)

guess_attempts = 1

user_guess = ''

play_again = 'Yes'

length_user_guess = len(user_guess)

while play_again.upper() == 'YES':
    print('Your hint is:', end='')
    for letter in secret_word:
        print('_ ', end='')
    print()
    user_guess = input('What is your guess?')
    length_user_guess = len(user_guess)
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
                else:
                    print('_ ', end='')
            guess_attempts += 1
            user_guess = input(' What is your guess?').upper()
            length_user_guess = len(user_guess)
    print(f'Congratulations you guessed it!\nIt took you {guess_attempts} tries.')
    play_again = input('Do you want to play again?')





            # for letter, char in zip(user_guess, secret_word):
            #     if letter == char:
            #         print(char.upper(), end='')
            #     elif letter in secret_word:
            #         print(letter.lower(), end='')
            #     else:
            #         print('_ ', end='')
# if len(user_guess) != len(secret_word):
#     print('Your guess must be the same length as the hint.')
#     guess_attempts = guess_attempts + 1

# print('Your hint is:', end='')
# for letter in secret_word:
#     print('_ ', end= '')

# print()

# while user_guess != secret_word:
#     user_guess = input('What is your guess?')
#     if user_guess == secret_word:
#         print(f'Congratulations! You guessed it!\nIt took you {guess_attempts} tries.')
#     else:
#         print('Your guess was not correct.')
#         if length_secret_word == len(user_guess):
#             for i in range(length_secret_word):
#                 if secret_word[i] == user_guess[i]:

#                 else:
#                     for letter in secret_word:
#                         print('_ ', end='')
#         else:
#             print('Your guess must be the same length as the hint provided.')
#         guess_attempts = guess_attempts + 1

