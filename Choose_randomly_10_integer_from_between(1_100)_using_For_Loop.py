# List contain twenty integer randomly using random module and find the all index position of a number,
# and that number taken from the user:-

import random

random_integers = []
for i in range(0, 20):
    random_integers.append(random.randint(1, 20))
print(random_integers)

receive_number = int(input("Enter the number from the keyboard:"))

output = []
for x in range(0, len(random_integers)):
    if random_integers[x] == receive_number:
        output.append(x)
if receive_number in random_integers:
    print("Index of receive number in the random integer list:", output)
else:
    print("Receive Number doesn't exist in a list")
