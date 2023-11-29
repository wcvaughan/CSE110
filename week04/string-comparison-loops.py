secret_word = "HORIZON"

user_guess = input("Guess the secret word.")

for letter in secret_word:
    user_guess.find(letter)
    print(letter, end='')
