file=open("integer_data","r")
for i in file:
    if int(i)%2==0:
        print(i,end="")
file.close()