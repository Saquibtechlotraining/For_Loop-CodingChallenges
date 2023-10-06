# Write a program to add all the elements of the list. Also find the length of the list using loop.

list = []
size = int(input("Enter the size of the list:"))
for i in range(0, size):
    elements = int(input(f"Enter the {i+1} element:"))
    list.append(elements)
print("List:", list)
print("Sum of all elements of the list:", sum(list))
print("Length of the list:",len(list))
