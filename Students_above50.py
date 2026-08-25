file = open("students.txt", "r")

for line in file:
    name, marks = line.split()
    
    marks = int(marks)

    if marks >= 50:
        print(name, marks)

file.close()