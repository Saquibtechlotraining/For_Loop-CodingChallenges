# Write a program to create a list of 10 numbers and print the list after replacing each number with the difference
# between itself and the previous number in the list. The first number should remain the same.

list = [2, 5, 9, 15, 23, 33, 45, 59, 75, 93]
output = [list[0]]                # append first value of list in output variable because 1 value of list not to change

for x in range(1, len(list)):
    val = list[x] - list[x-1]
    output.append(val)
print('List after replacing each number with the difference between itself and the previous number: ',output)

