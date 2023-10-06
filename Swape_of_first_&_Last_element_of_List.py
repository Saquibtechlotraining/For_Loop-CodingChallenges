# Given a list, write a Python program to swap first and last element of the list.

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Using New variable:-

def swapList(list):
    result = []
    for i in range(0, len(list)):
        if list[i] == list[0]:
            result.append(list[len(list)-1])
        elif list[i] == list[-1]:
            result.append(list[0])
        else:
            result.append(list[i])

    return result

list = [12, 35, 9, 56, 24]
print(swapList(list))


# Using Swapping:  # Taking temp variable to store while swiping.

def swaplist(list):
    temp = list[len(list)-1]
    list[-1] = list[0]
    list[0] = temp
    return list

list = [12, 35, 9, 56, 24]
print(swaplist(list))
