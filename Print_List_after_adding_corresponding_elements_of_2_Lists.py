# Write a program to create two lists of 5 numbers each and print
# the list after adding corresponding elements of the two lists.

list_1 = [10, 20, 30, 40, 50]
list_2 = [1, 2, 3, 4, 5]
output = []
for x, y in zip(list_1, list_2):
    output.append(x + y)
print("List after adding corresponding elements of list1 and list2:", output)  # [11, 22, 33, 44, 55]
