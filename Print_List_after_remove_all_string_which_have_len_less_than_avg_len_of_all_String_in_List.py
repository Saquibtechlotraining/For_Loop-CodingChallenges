# Write a program to create a list of 5 strings and print the list after removing all the strings
# which have a length less than the average length of all the strings in the list.

list = ["apple", "banana", "cherry", "date", "elderberry"]
combine_list_all_string = "".join(list)   # "applebananacherrydateelderberry"

avg_len_all_string = len(combine_list_all_string)/len(list)     # 31 / 5 = 6.2

output = []
for x in range(0, len(list)):
    if len(list[x]) >= avg_len_all_string:
        output.append(list[x])
    else:
        pass
print("List after removing all the strings with length less than the average length:", output)
