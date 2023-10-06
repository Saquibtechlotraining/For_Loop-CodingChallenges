# Take a sentence from user and print each word separated by ,(comma)

string = "I am a coder"
list_str = string.split()       # ['I', 'am', 'a', 'coder']
every_word = ",".join(list_str)    # I,am,a,coder
print(every_word)
print(type(every_word))