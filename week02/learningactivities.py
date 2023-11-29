import math
# Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
user_string = input('How old are you?')
user_age = int(user_string)
user_age_next_year = user_age + 1
print(f'You will be {user_age_next_year} next year.')

# Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
print('\n')
user_string_two = input('How many egg cartons do you have?')
user_egg_carton = int(user_string_two)
total_eggs = user_egg_carton * 12
print(f'You have {total_eggs} eggs!')

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
print('\n')
user_string_three = input('How many cookies will there be?')
cookie_num = int(user_string_three)
user_string_four = input('How many people are coming?')
people_num = int(user_string_four)
cookie_person = cookie_num / people_num
print(f'Each person will get {cookie_person} cookies.')

# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.
# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.
user_string_five = input('What is the temperature in Fahrenheit?')
user_temp_f = int(user_string_five)
user_temp_c = (user_temp_f - 32) * (5/9)
print(f'The temperature in Celsius is {user_temp_c:.1f}')