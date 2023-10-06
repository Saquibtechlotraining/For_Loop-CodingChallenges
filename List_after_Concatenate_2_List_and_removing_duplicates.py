# Write a program to create two lists of 5 numbers each and print the list after concatenating the two lists
# and removing duplicates.

list_1 = []
for i in range(0, 5):
    value_1 = int(input(f"Enter the {i+1} value in list 1:"))
    list_1.append(value_1)
print("List 1:", list_1)

list_2 = []
for j in range(0, 5):
    value_2 = int(input(f"Enter the {j+1} value in list 2:"))
    list_2.append(value_2)
print("List 2:", list_2)

final_list = sorted(set(list_1 + list_2))
print("List after concatenating two lists and removing duplicates:", final_list)
