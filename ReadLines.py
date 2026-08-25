file=open("student_details","r")
content=file.readlines()
for line in content:
    print(line,end="")
file.close()