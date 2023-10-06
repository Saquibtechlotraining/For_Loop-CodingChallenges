# Write a python program to take a list of numbers and print the list of squares of those numbers.

list = []
size = int(input("Enter the size of the list:"))
for i in range(0, size):
    number = int(input(f"Enter the {i+1} number:"))
    list.append(number)
print("List:", list)       # List: [9, 12, 14]

result = [num ** 2 for num in list]
print("List of numbers after squares of these numbers:", result)  # [81, 144, 196]