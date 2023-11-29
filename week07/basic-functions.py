def display_regular(user_input):
    print(user_input)
def display_uppercase(user_input):
    user_input = user_input.upper()
    print(user_input)
def display_lowercase(user_input):
    user_input = user_input.lower()
    print(user_input)

print('Let\'s do some stuff.')

your_message = input("Type any sentence you want.")

display_regular(your_message)
display_uppercase(your_message)
display_lowercase(your_message)