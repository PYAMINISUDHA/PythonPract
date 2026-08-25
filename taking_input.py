file = open("names.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()