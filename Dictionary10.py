students = {
    "yamini": 95,
    "varshitha": 92,
    "Amit": 90,
    "Sneha": 95
}
highest_student =""
highest_marks =0
for name,marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name
print("Student:", highest_student)
print("Marks:", highest_marks)
