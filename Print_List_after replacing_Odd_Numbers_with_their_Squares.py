# Write a program to create a list of 5 numbers and print the list after replacing all the odd numbers
# with their squares:-

list = []
for i in range(0, 5):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)

output = []
for val in list:
    if (val % 2) != 0:
        output.append(val ** 2)
    else:
        output.append(val)
print("Original List:", list)
print("List after replacing all odd numbers with their Squares:", output)