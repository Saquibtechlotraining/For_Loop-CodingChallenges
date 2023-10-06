# Write a python program to find the common elements between two lists:-

list_1 = []
size_1 = int(input("Enter the size of list 1:"))
for i in range(0, size_1):
    value_1 = int(input(f"Enter the {i+1} element in the list 1:"))
    list_1.append(value_1)
print("List 1:", list_1)

list_2 = []
size_2 = int(input("Enter the size of list 2:"))
for j in range(0, size_2):
    value_2 = int(input(f"Enter the {j+1} element in the list 2:"))
    list_2.append(value_2)
print("List 2:", list_2)

output = []
for ind in range(0, len(list_1)):
    for indx in range(0, len(list_2)):
        if list_1[ind] == list_2[indx]:
            output.append(list_1[ind])
print("Common elements between two lists:", output)


