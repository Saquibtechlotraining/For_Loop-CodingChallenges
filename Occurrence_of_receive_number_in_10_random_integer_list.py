# Print the Occurrence of Receive Number in Random Integer List using random Module:-

import random
random_integers = []
for i in range(0, 10):
    random_integers.append(random.randint(1, 20))
print("Random integers List:",random_integers)

receive_number = int(input("Enter the number from the keyboard:"))

count = 0
for num in random_integers:
    if receive_number == num:
        count = count + 1
print("Occurrence of receive number in random integers list:", count)