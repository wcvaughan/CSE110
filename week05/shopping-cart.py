#Added logic to indicate to shopper that their cart is empty when selecting view cart at the beginning, 

#to ask to remove items from their cart, or ask for a total prior to adding items to their cart.

print('Welcome to the shopping cart program!')

items = []

prices = []

total_cost = 0

user_selection = 0

user_selection = int(input('Please select from one the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))

while user_selection != '':

    if user_selection <= 5:

        if user_selection == 1:
            user_item = input('What item would you like to add?')
            item_price = float(input('What is the price of this item?'))
            items.append(user_item)
            prices.append(item_price)
            print(f'\'{user_item}\' has been added to the cart.')
            user_selection = int(input('Please select from one the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))

        elif user_selection == 2:

            if len(items) == 0:
                print('Your shopping cart is empty. Please add some items to your cart.')

            else:
                print(f'The contents of the shopping cart are:')
                for i in range(len(items)):
                        item = items[i]
                        print(f'{i + 1}. {item} - ${prices[i]:.2f}')
                user_selection = int(input('Please select from one the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))

        elif user_selection == 3:

            if len(items) == 0:
                print('Your shopping cart is empty. Please add some items to your cart.')

            else:
                item_remove = int(input('Which item do you want to remove from the cart? Please use the number of the item.'))

                if item_remove > len(items):
                    print('I\'m sorry that is not a valid choice.')

                else:
                    items.pop(item_remove - 1)
                    prices.pop(item_remove - 1)
                user_selection = int(input('Please select from one the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))

        elif user_selection == 4:

            if len(items) == 0:
                print('Your shopping cart is empty. Please add some items to your cart.')

            else:
                for i in range(len(prices)):
                    total_cost = total_cost + prices[i]
                print(f'The total comes to: ${total_cost:.2f}')
                total_cost = 0
            user_selection = int(input('Please select from one the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))

        elif user_selection == 5:
            print('Thank you for shopping with us! Please come back soon.')
            break
    else:
        print('I\'m sorry that is not a valid choice.')