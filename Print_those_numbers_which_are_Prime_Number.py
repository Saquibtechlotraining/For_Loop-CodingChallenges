# Write a program to create a list of numbers and print only those numbers which are prime numbers:-

list = []
size = int(input("Enter the size:"))
for i in range(0, size):
    value = int(input(f"Enter the {i+1} value:"))
    list.append(value)

output = []
for num in list:
    if (num % 2) != 0:
        output.append(num)
print(output)