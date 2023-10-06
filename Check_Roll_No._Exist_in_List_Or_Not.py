# Create a List of student roll numbers of 5 students and take a roll number from user to search in the list.
# Print if it exists in the list or not.

list = []
for i in range(0, 5):
    students_roll_no = int(input(f"Enter the {i+1} student roll number:"))
    list.append(students_roll_no)
print("List of 5 Students Roll Number:", list)

search_roll_no = int(input("Enter the roll number to be search in a list:"))
if search_roll_no in list:
    print("Yes" ,search_roll_no, "roll number exist in a list")
else:
    print("Roll Number not exist in a list")
