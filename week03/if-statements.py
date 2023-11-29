# Write a program that asks the user for two integers.

# Then, write three separate if/else statements as follows:

# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

user_input = input('Give me a number.')

user_num_one = int(user_input)

user_input = input('Give me a second number.')

user_num_two = int(user_input)

#The following version separates the if else statements but does not necessarily provide the correct responses

# if user_num_one > user_num_two:
#     print('The first number is greater.')
# else:
#     print('The first number is not greater.')

# if user_num_one == user_num_two:
#     print('The numbers are equal.')
# else:
#     print('The numbers are not equal.')

# if user_num_one < user_num_two:
#     print('The second number is greater.')
# else:
#     print('The second number is not greater.')


#The following would be a cleaner version which provides correct responses

if user_num_one > user_num_two:
    print('The numbers are not equal.')
    print('The first number is greater.')
    print('The second number is not greater.')
elif user_num_one < user_num_two:
    print('The numbers are not equal.')
    print('The second number is greater.')
    print('The first number is not greater.')
elif user_num_one == user_num_two:
    print('The numbers are equal.')

# Have the program ask the user for their favorite animal. Then write an if statement as follows:

# Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). 

# If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

user_fav_animal = input('What is your favorite animal?')

my_fav_animal = "moose"

if user_fav_animal.lower() == my_fav_animal.lower():
    print('That\'s my favorite animal too!')
else:
    print('That is not my favorite animal')

# Verify that your program works correctly by following each step in this testing procedure:

# Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

# Test it with two numbers that are equal. Verify that all three values that are printed are correct.

# Test the second part of your program with an animal that is different. Verify that the correct message is shown.

# Test it with an animal that is the same. Verify that the correct message is shown.

# Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.