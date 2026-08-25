name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Marks: " + marks + "\n")

file.close()


file = open("student.txt", "r")

content = file.read()

print("\nStudent Information:")
print(content)

file.close()