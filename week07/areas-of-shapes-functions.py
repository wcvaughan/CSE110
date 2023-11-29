# Write a function compute_area_square that accepts a single 

# value as a parameter, and then computes the area and returns it.

# Below the function, write code to prompt the user for the 

# side of a square and save it into a variable, then pass this 

# variable to the function to compute the area. Finally, get 

# the result back from the function and display it.

# Repeat the previous step to write and test the functions 

# compute_area_rectangle and compute_area_circle.

# Write a loop to ask the user what kind of shape they have, 

# then prompt for the length of a side, or sides, or radius, 

# and then calls the appropriate function, and displays the 

# result. The program should continue looping until the user enters "quit" for the shape.

# Recognize that you can compute the area of a square by 

# passing the task along to a function that computes the 

# areas of rectangles, by giving it the side of the square twice.

# Change your program so that the compute_area_square function

# doesn't compute the area directly, but instead calls the 

# compute_area_rectangle to do the work. It should pass 

# the square side length to it (twice) and then return the 

# value that the compute_area_rectangle function computes.



def compute_area_square(x):
    square_area = x ** 2
    return square_area

def compute_area_rectangle(x, y):
    rectangle_area = x * y
    return rectangle_area

def compute_area_circle(r):
    circle_area = 3.14 * (r ** 2)
    return circle_area

def compute_area_square_two(x):
    rectangle_area_two = compute_area_rectangle(x, x) 
    return rectangle_area_two

user_shape = input('What is your shape?')
while user_shape.lower() != 'quit':
    if user_shape.lower() == 'square':
        user_value = int(input('What is the length of a side of your square?'))
        print(compute_area_square_two(user_value))
        user_shape = input('What is your shape?')
    elif user_shape.lower() == 'rectangle':
        user_length = int(input('What is the length of a side of your rectangle?'))
        user_width = int(input('What is the width of a side of your rectangle?'))
        print(compute_area_rectangle(user_length, user_width))
        user_shape = input('What is your shape?')
    elif user_shape.lower() == 'circle':
        user_radius = int(input('What is the radius of your circle?'))
        print(compute_area_circle(user_radius))
        user_shape = input('What is your shape?')
