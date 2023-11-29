#The last name should be converted from whatever the user types to be displayed in ALL CAPS.

# The job title should be displayed so that the first letter is capitalized.

# The email address should be displayed in all lowercase.

print('What is your first name?')
first_name = input()
first_name_id = first_name.title()
print('What is your last name?')
last_name = input()
last_name_id = last_name.upper()
print('What is your email address?')
email_address = input()
print('What is your phone number?')
phone_number = input()
print('What is your job title?')
job_title = input()
job_title_id = job_title.capitalize()
print('What is your ID number?')
id_number = input()
print('What is your eye color?')
eye_color = input()
eye_color_id = eye_color.capitalize()
print('What is your hair color?')
hair_color = input().ljust(20, ' ')
hair_color_id = hair_color.capitalize()
print(f'Hair Color: {hair_color_id} Eye Color: {eye_color_id}')
print('What month did you start?')
start_month = input().ljust(20, ' ')
start_month_id = start_month.capitalize()
print(f'Month: {start_month_id}')
print('Have you completed advanced training?')
training = input()
training_id = training.capitalize()
print(f'Training: {training_id}')

print(f'First Name: {first_name}\nLast Name: {last_name}\nEmail Address: {email_address}\nPhone Number: {phone_number}\nJob Title: {job_title}\nID Number: {id_number}')
print(f'The ID Card is:\n----------------------------------------\n{last_name_id}, {first_name_id}\n{job_title_id}\nID: {id_number}\n\n{email_address}\n{phone_number}\nHair color: {hair_color_id}Eye Color: {eye_color_id}\nMonth: {start_month_id}Training: {training_id}\n----------------------------------------')