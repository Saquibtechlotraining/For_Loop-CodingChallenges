# Write a python program to remove duplicates from a list.

list_1 = []
size = int(input("Enter the size of the list:"))
for i in range(0, size):
    number = int(input(f"Enter the {i+1} number:"))
    list_1.append(number)
print("List before removing duplicates:", list_1)              # [45, 15, 45, 15, 85]
print("List after removing duplicates:", list(set(list_1)))    # [85, 45, 15]

