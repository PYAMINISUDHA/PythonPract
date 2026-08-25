filename = input("Enter the filename: ")
 
try:
    file = open(filename, "r")
 
    print(file.read())
 
    file.close()
 
except FileNotFoundError:
    print("File does not exist.")
 
except Exception as e:
    print("An unexpected error occurred:", e)