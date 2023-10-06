# Write a python program to create a list of numbers.
# Print the sum of the elements of even index and odd index separately.
# 0 is considered as even.

list = []
size = int(input("Enter the size of list:"))
for i in range(0, size):
    value = int(input(f"Enter the value of {i} index:"))
    list.append(value)
print("List:", list)

even_sum = list[0]
odd_sum = 0
for x in range(1, len(list)):
    if (x % 2) == 0:
        even_sum = even_sum + list[x]
    else:
        odd_sum = odd_sum + list[x]

print("Sum of elements of even index:", even_sum)
print("Sum of elements of odd index:", odd_sum)