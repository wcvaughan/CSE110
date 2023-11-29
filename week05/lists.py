friend = ''

friends = []

while friend.lower() != 'end':
    friend = input('Type the name of a friend:').capitalize()
    if friend.lower() != 'end':
        friends.append(friend)

print()
print('Your friends are:')
for friend in friends:
    print(friend)
