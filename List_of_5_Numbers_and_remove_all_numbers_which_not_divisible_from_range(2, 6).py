# Write a program to create a list of 5 numbers and print the list after removing all the numbers
# which are not divisible by any number in the range 2 to 5.

list = []
for i in range(0, 5):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)
print("Original List:", list)   # Original List: [15, 10, 7, 24, 33]

output = []
for num in list:
    for i in range(2, 6):
        if (num % i) == 0:
            output.append(num)
            break

print('List after removing all the numbers which are not divisible by any number in the range 2 to 5: ', output)
