file = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()


file = open("students.txt", "r")

serial_number = 1

for name in file:
    print(serial_number, name, end="")
    serial_number = serial_number + 1

file.close()