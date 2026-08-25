# Create notes.txt and write some initial text
file = open("notes.txt", "w")
file.write("This is my first note.\n")
file.close()
 
# Take a new sentence from the user
sentence = input("Enter a new sentence: ")
 
# Append the sentence to the existing file
file = open("notes.txt", "a")
file.write(sentence + "\n")
file.close()
 
# Read and display the complete file
file = open("notes.txt", "r")
 
for line in file:
    print(line, end="")
 
file.close()