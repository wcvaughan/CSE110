# Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade.
#  (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

user_grade_percentage = float(input('What is your grade percentage?'))

# if user_grade_percentage >= 90:
#     print('Your grade is: A')
# elif user_grade_percentage >= 80:
#     print('Your grade is: B')
# elif user_grade_percentage >= 70:
#     print('Your grade is: C')
# elif user_grade_percentage >= 60:
#     print('Your grade is: D')
# else:
#     print('Your grade is: F')

# Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out.
#  Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them.
#  If not, display a different message to encourage them for next time.

# if user_grade_percentage >= 70:
#     print('Congratulations on passing the course!')
# else:
#     print('Consider reaching out for help in passing this course in the future.')

# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block,
# instead create a new variable called letter and then in each block, set this variable to the appropriate value.
# Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.

# if user_grade_percentage >= 90:
#     letter = "A"
# elif user_grade_percentage >= 80:
#     letter = "B"
# elif user_grade_percentage >= 70:
#     letter = "C"
# elif user_grade_percentage >= 60:
#     letter = "D"
# else:
#     letter = "F"
# print(f'Your grade in this course is: {letter}')

# if user_grade_percentage >= 70:
#     print('Congratulations on passing the course!')
# else:
#     print('Consider reaching out for help in passing this course in the future.')

# Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-.

if user_grade_percentage >= 90:
    letter = "A"
elif user_grade_percentage >= 80:
    letter = "B"
elif user_grade_percentage >= 70:
    letter = "C"
elif user_grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

# For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

# After your logic to determine the grade letter, add another section to determine the sign.

# Save this sign into a variable. Then, display both the grade letter and the sign in one print statement.

# Hint: To get the last digit, you could divide the number by 10, and get the remainder.

# You might refer back to the Week 02 preparation material to see the operators and find the one that does division and gives you the remainder.

# At this point, don't worry about the exceptional cases of A+, F+, or F-.

user_grade_quality = user_grade_percentage % 10

if user_grade_quality >= 7:
    quality = '+'
elif user_grade_quality < 3:
    quality = '-'
else:
    quality = ' '

# Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

# Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.

if letter == 'F':
    quality = ' '

if user_grade_percentage > 96:
    quality = ' '

print(f'Your grade in this course is: {letter}{quality}')

if user_grade_percentage >= 70:
    print('Congratulations on passing the course!')
else:
    print('Consider reaching out for help in passing this course in the future.')




