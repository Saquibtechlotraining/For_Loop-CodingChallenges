# Write a python program to create a list and sort it using the built-in function of list in descending order:-

list = []
size = int(input("Enter the size of the list:"))
for i in range(0, size):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)
list.sort(reverse=True)
print("Sort a List in Descending Order:", list)
print("Largest number in the list:", max(list))
print("Smallest number in the list:", min(list))