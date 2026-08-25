filename = input("Enter the filename: ")
 
try:
    file = open(filename, "x")
    file.write("This is a new file.")
    file.close()
 
    print("File created successfully.")
 
except FileExistsError:
    print("File already exists.")