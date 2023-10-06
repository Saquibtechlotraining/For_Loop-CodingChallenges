# Write a program to create a list of 5 numbers and print the list after inserting a new number at the beginning
# of the list and sorting the list in ascending order.

list = []
for i in range(0, 5):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)
print("Original List:", list)       # Original List: [45, 784, 45, 65, 85]
new_number = int(input("Insert this new number at the beginning of the list:"))   # 99
list.insert(0, new_number)
print("List after inserting new number at the beginning of the list:", list)   # [99, 45, 784, 45, 65, 85]
list.sort()
print("List after sorting in ascending order:", list)      # [45, 45, 65, 85, 99, 784]

