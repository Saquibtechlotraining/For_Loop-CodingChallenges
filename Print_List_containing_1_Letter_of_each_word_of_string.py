# Method-1 Take a sentence from user and create a list and print the list of first letter of each word
# in the first list:-

st = "I am working as datascientist"
split_string = st.split()
output = []
for x in range(0, len(split_string)):
    output.append((split_string[x])[0])
print("List of first letter of each word of string:",output)

# Method-2 Take a sentence from user and create a list and print the list of first letter of each word
# in the first list:-

st = "I am working as datascientist"
split_string = st.split()
output = [word[0] for word in split_string]
print("List of first letter of each word of string:",output)