
# Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
nums = []

num = None

while num != 0:
    num = int(input('Give me a series of positive integers to add them to the list. To stop adding enter \'0\''))
    if num != 0:
        nums.append(num)

sum = 0

average = 0

# Once you have a list, have your program do the following:

# Compute the sum, or total, of the numbers in the list.

for i in range(len(nums)):
    sum += nums[i]

print(f'Sum: {sum}')
print()

# Compute the average of the numbers in the list.

average = sum / (len(nums) + 1)

print(f'Average: {average}')
print()
# Find the maximum, or largest, number in the list.

max_num = max(nums)

print(f'Max number: {max_num}')
print()
min_num = min(nums)

print(f'Min number: {min_num}')
print()
# Stretch Challenges ##

# Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

nums = []

num = None

pos_nums = []

while num != 0:
    num = int(input('Give me a series of positive and negative integers to add them to the list. To stop adding enter \'0\''))
    if num != 0:
        nums.append(num)

for i in range(len(nums)):
    if nums[i] > 0:
        pos_nums.append(nums[i])

print(f'Smallest positive number: {min(pos_nums)}')

# for i in range(len(nums)):
#     num = abs(num)

# Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

sort_nums = sorted(nums)

print(f'Original: {nums}')
print(f'Sorted: {sort_nums}')

