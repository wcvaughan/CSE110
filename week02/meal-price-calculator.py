# The user is prompted regarding a tip and offered a few options of tip and asked to provide their choice as whole number. The tip is calculated and added to the new meal total.





# Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. 

# Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

# Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

# Ask the user for the following:

# The price of a child's meal (floating point)

child_meal_price_input = float(input('What is the price of a child\'s meal?'))

child_meal_price = child_meal_price_input

# The price of an adult's meal (floating point)

adult_meal_price_input = float(input('What is the price of a adult\'s meal?'))

adult_meal_price = adult_meal_price_input

# The number of children (integer)

num_children_input = int(input('How many children are eating?'))

num_children = num_children_input

# The number of adults (integer)

num_adult_input = int(input('How many adult are eating?'))

num_adult = num_adult_input

# Then, complete the following steps:

# Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and 

# multiplying the number of adults by the price of their meal and adding those two values together.

meal_total = (num_children * child_meal_price) + (num_adult * adult_meal_price)

# Display the subtotal.

print(f'The total price before sales tax is: ${meal_total:.2f} ')

## COMPLETE TO THIS POINT BY MID WEEK ##

# Ask the user for the sales tax rate as a percentage (floating point). Please note that this percentage should be entered and

# stored as a number such as 6, or 6.5, not 0.06 or 0.065.

sales_tax_input = float(input('What is the sales tax rate?'))

sales_tax_num = sales_tax_input

sales_tax = sales_tax_num / 100

# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

print(f'The sales tax rate is {sales_tax_num:.0f}%')

print(f'The sales tax for this meal is ${meal_total * sales_tax:.2f}')

# Compute and display the total price of the meal by adding the subtotal and the sales tax.

meal_total_w_tax = meal_total + (meal_total * sales_tax)

print(f'Your meal comes to: ${meal_total_w_tax:.2f}')

# Finally:

# Ask the user for the the payment amount (floating point)

user_cash_input = float(input('Paying with how much cash?'))

user_cash = user_cash_input

# Compute and display the change.

user_change = user_cash - meal_total_w_tax

print(f'Your change is: ${user_change:.2f}')

# For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage,

# or anything else you can think of. Play around with different ideas and see what you can learn!

user_tip_input = float(input('You wanted to leave a tip? My apologies. Please choose between 10%, 15%, 20%, or if you are feeling generous a 99% tip. Please use whole numbers, not decimals. '))

user_tip_whole = user_tip_input

user_tip = user_tip_whole / 100

new_meal_total = meal_total_w_tax + (meal_total * user_tip)

print(f'Your new total is: ${new_meal_total:.2f}')

user_cash_input = float(input('Paying with how much cash?'))

user_cash = user_cash_input

user_change = user_cash - new_meal_total

print(f'Your change is: ${user_change:.2f}')
