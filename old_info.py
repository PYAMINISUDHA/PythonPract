# Create a file with old information
file = open("info.txt", "w")
file.write("Old information\n")
file.write("This information will be replaced.\n")
file.close()
 
# Take new information from the user
new_info = input("Enter new information: ")
 
# Open in "w" mode and overwrite the old content
file = open("info.txt", "w")
file.write(new_info + "\n")
file.close()
 
# Read the file to verify the change
file = open("info.txt", "r")
 
for line in file:
    print(line, end="")
 
file.close()