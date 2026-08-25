file = open("names.txt", "r")

count = 0

for name in file:
    print(name, end="")
    count = count + 1

print("\nTotal names:", count)

file.close()