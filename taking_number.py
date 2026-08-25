file = open("numberss3 .txt", "w")

for i in range(5):
    num = input("Enter number: ")
    file.write(num + "\n")

file.close()