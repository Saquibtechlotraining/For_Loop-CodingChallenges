# Write a program to merge two lists into a single list without using the built-in extend() or + operators.
# Example
# input: [1, 2, 3], [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

for num in list_2:
    list_1.append(num)    # Adding every element of list_2 in list_1
print("Merged two list:",list_1)
