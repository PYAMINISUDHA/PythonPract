import os
 
filename = input("Enter the filename to delete: ")
 
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File does not exist.")