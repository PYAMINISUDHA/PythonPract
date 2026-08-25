file=open("student_details","r")
line=file.readline()
while line:
    print(line,end="")
    line=file.readline()
file.close()