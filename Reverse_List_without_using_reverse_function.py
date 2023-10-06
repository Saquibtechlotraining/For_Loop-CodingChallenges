# Reverse list without using reverse function:-

# Method-1 (with using Slicing):-

list = ["saquib", "ahmad", 63]
print(list[::-1])                     # [63, 'ahmad', 'saquib']

# Method-2 (Iterating from the reverse order):-

output = []
list = ["saquib", "ahmad", 63]
for i in range(len(list)-1, -1, -1):
    output.append(list[i])
print(output)                          # [63, 'ahmad', 'saquib']
