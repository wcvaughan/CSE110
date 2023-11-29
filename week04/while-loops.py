# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.
user_num = 0
user_num = int(input('Give me a positive number'))
while user_num < 0:
    user_num = int(input('Give me a positive number'))
print(user_num)
# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."
parent_answer = 'NO'

while parent_answer == "NO":
    parent_answer = input('Can I have a piece of candy?')
    parent_answer = parent_answer.upper()

print('Thank you.')


# For the positive number program, enter several negative numbers, then a positive one.

# Try entering a positive number first, and ensure that it doesn't ask again.

# Try entering 0 and ensure that it correctly treats it as a positive number.

# For the piece of candy program, test your last loop by entering different amounts of no's before finally saying yes.

# Try saying "yes" the very first time, and ensure that it works as expected.