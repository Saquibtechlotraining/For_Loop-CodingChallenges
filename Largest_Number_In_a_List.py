# Create a list of ten numbers and print the largest number in the list.

list = []
for i in range(0, 10):
    number = int(input(f"Enter thr {i+1} number in a list:"))
    list.append(number)
print("List:", list)
print("Largest Number in the list:", max(list))

