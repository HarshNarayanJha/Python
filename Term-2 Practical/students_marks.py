# Create a dictionary with the roll number, name and marks of n students in a class
# and display the names of students who have scored marks above 75

data = {}

while True:
    roll = input("Enter Roll No. (enter blank to stop)>> ")
    if not roll:
        break

    name = input("Name of student >> ")
    marks = int(input("Marks of student >> "))

    data[int(roll)] = (name, marks)

print("Printing Students who have scored above 75...\n")
print("Student Name (roll)\tMarks")

for roll in data:
    if data[roll][1] > 75:
        print(f"{data[roll][0]} ({roll})\t{data[roll][1]}")