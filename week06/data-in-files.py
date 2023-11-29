# Iterate through the list and display each string to the screen.

# Split the string into a name and age and print them to the screen.

# Find the age that is the youngest.

# Keep track of the name of the person that is the youngest.

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 200

youngest_person = ''

for person in people:
    person = person.split()
    name = person[0]
    age = int(person[1])
    if age < min_age:
        min_age = age

        youngest_person = name
    
print(f'The youngest person is {youngest_person} at age {min_age}')
