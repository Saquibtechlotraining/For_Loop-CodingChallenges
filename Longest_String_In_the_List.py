# Given a list of strings, write a program to find the longest string in the list.
# Example
# input: ['hi', 'world', 'how', 'are', 'you']
# Output: 'world'

list = ["hi", "world", "how", "are", "you"]
longest = ""

for string in list:
    if len(string) > len(longest):
        longest = string
print("Longest string in the list:", longest)