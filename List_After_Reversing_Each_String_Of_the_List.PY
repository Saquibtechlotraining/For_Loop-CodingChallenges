# Write a program to create a list of 5 strings and print the list after converting each string in the list:-

list = []
for i in range(0, 5):
    value = input(f"Enter the {i+1} string:")
    list.append(value)
print("List before converting:", list)    # ['lenovo', 'coder', 'consoleFlare', 'python', 'datascience']

output = []
for string in list:
    output.append(string[::-1])
print("List after converting:", output)   # ['ovonel', 'redoc', 'eralFelosnoc', 'nohtyp', 'ecneicsatad']

