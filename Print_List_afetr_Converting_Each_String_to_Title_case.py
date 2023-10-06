# Write a program to create a list of 5 strings and print the list after converting each string to title case:-

list = []
for i in range(0, 5):
    word = input(f"Enter the {i+1} string:")
    list.append(word)

output = []
for string in list:
    output.append(string.title())
print("List after converting each string to title case:", output)

