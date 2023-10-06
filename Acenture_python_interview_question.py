# Given a list of alpha numeric values. Sort the below list with the numerical values in each string
# in ascending order
# Output:- ['Zaid30', 'Mukesh50', 'Nisha99', 'Monu100', 'sam200']

lst = ['sam200', 'Monu100', 'Zaid30', 'Mukesh50', 'Nisha99']

result = []
for value in lst:
    data = ""
    for char in value:
        if char.isdigit():
            data = data+char
    result.append(data)               # ['30', '50', '99', '100', '200']

for val in range(0, len(result)):
    result[val] = int(result[val])
result.sort()                         # [30, 50, 99, 100, 200]

output = []
for digit in result:
    for values in lst:
        if str(digit) in values:
            output.append(values)
print(output)