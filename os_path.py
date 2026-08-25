import os
 
filename = input("Enter the filename: ")
 
if os.path.exists(filename):
    print("File exists.")
 
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("File does not exist.")