# Write a program to create a list of numbers and print the list of numbers after reversing each number in the list:-

output = []
list = [45, 2355, 4240, 4, 315]
for i in range(len(list)-1, -1, -1):
    output.append(list[i])
print("List after reversing each number in the list:", output)   #  [315, 4, 4240, 2355, 45]