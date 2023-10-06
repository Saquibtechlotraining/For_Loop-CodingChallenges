# Write a program to create a list of 5 strings and print the list after removing all the vowels from the
# first and last strings in the list.

result = []
list = ["apple", "banana", "cherry", "date", "elderberry"]
for x in range(0, len(list)):
    value = list[x].replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    result.append(value)
print(result)             # ['ppl', 'bnn', 'chrry', 'dt', 'ldrbrry']