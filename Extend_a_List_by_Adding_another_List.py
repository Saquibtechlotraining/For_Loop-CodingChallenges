# Write a python program to extend a list by adding another list:-

list_1 = []
size_1 = int(input("Enter the size of the list1:"))
for i in range(0, size_1):
    value_1 = int(input(f"Enter the {i+1} value in list1:"))
    list_1.append(value_1)
print("List 1:", list_1)

list_2 = []
size_2 = int(input("Enter the size of the list 2:"))
if size_2 <= 0:
    print("List_2 element can't be adding in another list 1 because of size of list 2 is 0:")
else:
    for j in range(0, size_2):
        value_2 = int(input(f"Enter the {j+1} value in list2:"))
        list_2.append(value_2)
    print("List 2:", list_2)

    list_1.extend(list_2)
    print("List 2 is extended in list 1:", list_1)
