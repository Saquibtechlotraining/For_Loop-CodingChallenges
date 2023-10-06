# Given a list of integers, write a program to find the sum of all even numbers in the list.
# Example
# input: [1, 2, 3, 4, 5, 6]
# Output: 12

output = []
list = [1, 2, 3, 4, 5, 6]
for i in range(0, len(list)):
    if (list[i] % 2) == 0:
        output.append(list[i])
print(sum(output))
