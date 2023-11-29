import math
# Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:

# Make sure that your program can appropriately handle decimal values as well as whole numbers.

# Square—The area is the length of a side squared.

# Rectangle—The area is the length multiplied by the width.

# Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

square_length_input = input('What is the length of the side of your square?')

square_length = float(square_length_input)

square_area = square_length ** 2

print(f'The area of your square is {square_area} units squared')

rectangle_length_input = input('What is the length of the side of your rectangle?')

rectangle_length = float(rectangle_length_input)

rectangle_width_input = input('What is the width of the side of your rectangle?')

rectangle_width = float(rectangle_width_input)

rectangle_area = rectangle_length * rectangle_width

print(f'The area of your rectangle is {rectangle_area} units squared')

circle_radius_input = input('What is the radius of your circle?')

circle_radius = float(circle_radius_input)

circle_area = 3.14 * (circle_radius ** 2)

print(f'The area of your circle is {circle_area} units squared')

# The stretch challenges for this activity are:

# Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module. 

# Hint, you might try searching on the internet for something like, "python how to get the value of pi."

circle_radius_input_stretch = input('What is the radius of your circle?')

circle_radius_stretch = float(circle_radius_input_stretch)

circle_area_stretch = math.pi * (circle_radius_stretch ** 2)

print(f'The area of your circle is {circle_area_stretch} units squared')

# Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, 

# and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

user_value_input = input('Provide a positive integer or decimal value.')

user_value = float(user_value_input)

square_stretch = user_value ** 2

circle_stretch = math.pi * (user_value ** 2)

cube_stretch = user_value ** 3

sphere_stretch = (4/3) * math.pi * (user_value ** 3)

print(f'Provided your value the volume of a square with length {user_value} units is {square_stretch} units squared')

print(f'Provided your value the volume of a circle with radius {user_value} units is {circle_stretch} units squared')

print(f'Provided your value the volume of a cube with length {user_value} units is {cube_stretch} units cubed')

print(f'Provided your value the volume of a sphere with radius {user_value} units is {sphere_stretch} units cubed')


# For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. Then, display the 

# resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.

square_length_input_stretch_two = input('What is the length of the side of your square in centimeters?')

square_length_stretch_two = float(square_length_input_stretch_two)

square_area_stretch_centimeters = square_length_stretch_two ** 2

square_area_stretch_meters = (square_length_stretch_two / 100) ** 2

print(f'The area of your square is {square_area_stretch_centimeters} centimeters squared')

print(f'The area of your square is {square_area_stretch_meters} meters squared')

rectangle_length_input_stretch_two = input('What is the length of the side of your rectangle in centimeters?')

rectangle_length_stretch_two = float(rectangle_length_input_stretch_two)

rectangle_width_input_stretch_two = input('What is the width of the side of your rectangle in centimeters?')

rectangle_width_stretch_two = float(rectangle_width_input_stretch_two)

rectangle_area_stretch_centimeters = rectangle_length_stretch_two * rectangle_width_stretch_two

rectangle_area_stretch_meters = (rectangle_length_stretch_two / 100) * (rectangle_width_stretch_two / 100)

print(f'The area of your rectangle is {rectangle_area_stretch_centimeters} centimeters squared')

print(f'The area of your rectangle is {rectangle_area_stretch_meters} meters squared')

circle_radius_input_stretch_two = input('What is the radius of your circle in centimeters?')

circle_radius_stretch_two = float(circle_radius_input_stretch_two)

circle_area_stretch_centimeters = math.pi * (circle_radius_stretch_two ** 2)

circle_area_stretch_meters = math.pi * ((circle_radius_stretch_two / 100) ** 2)

print(f'The area of your circle is {circle_area_stretch_centimeters} centimeters squared')

print(f'The area of your circle is {circle_area_stretch_meters} meters squared')