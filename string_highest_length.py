names=["java","python","dbms","c#","oracle"]
file=open("names","w")
for i in names:
    file.write(i+"\n")
file.close()
file=open("names","r")
name=file.readline()
while name:
    if len(name)>5:
        print(name,end="")
    name=file.readline()
file.close()