requested_toppings = ['mushrooms', 'green-peppers', 'extra-cheese', 'Beef', 'Carrot']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print("\nFinished making your Pizza\n")


users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello Chidy would you like to see a status report?')
        else:
            print(f'Hello {user} thank you for logging again')
else:
    print("We need to find some users")


alien_0 = {'color': 'green', 'value': '5pts'}
print(alien_0['color'])