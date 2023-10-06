# Suppose a list contains positive and negative numbers.
# Write a program to create two lists - one containing positive numbers and another containing negative numbers.

list = []
size = int(input("Enter the size of the list:"))
for i in range(0, size):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)
print("Original List:", list)

positive_list = []
negative_list = []

for num in list:
    if num >= 1:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)
    else:
        pass

print("List of +ve number:", positive_list)
print("List of -ve number:", negative_list)
