grocery = ''

grocery_list = []

while grocery.lower() != 'quit':
    grocery = input('What is next on your grocery list?: (type quit to finish)').capitalize()
    if grocery.lower() != 'quit':
        grocery_list.append(grocery)

print()
print('Your grocery list is:')
for i in range(len(grocery_list)):
    grocery = grocery_list[i]

    print(f'{i}. {grocery}')

print('We need to replace an item.')
item_num = int(input('Give me the item #'))
item_name = input('What is the new item name?')

grocery_list[item_num] = item_name.capitalize()

print()
print('Your grocery list is:')
for i in range(len(grocery_list)):
    grocery = grocery_list[i]

    print(f'Item: {i} . {grocery}')