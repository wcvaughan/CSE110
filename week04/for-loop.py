# Given the following list of items (copy and paste this line into your program):

# Use a for loop to iterate through this list one by one and display each item on its own line as follows:

# Use a for loop to display the numbers 1–8, one number on each line as follows:

# Use a for loop to display the even numbers (hint: count by two) 2–20, one number on each line as follows:
    
# Verify that the colors display as desired.

# Verify that your output for part 2 does not include 0.

# Verify that your output for part 2 does not include 9.

# Verify that your output for part 3 does not include any odd numbers.

# Verify that your output for part 3 starts at 2 and ends at 20.

colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

print()

for i in range(1, 9):
    print(i)

print()

for i in range(2, 21, 2):
    print(i)