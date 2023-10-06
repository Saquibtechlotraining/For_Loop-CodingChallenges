# Create a ten numbers and print only the even numbers in the list
size = 10
list = []
for i in range(0, size):
    number = int(input(f"Enter the {i+1} number:"))
    list.append(number)
print("List of 10 numbers:", list)

list_1 =[]
for num in range(0, len(list)):
    if list[num] % 2 == 0:
        list_1.append(list[num])
print("List of even numbers:", list_1)