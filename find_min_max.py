min=None
max=None
file=open("integer_data","r")
num=file.readline()
for i in num:
    if i>max:
        max=i
    if i<min:
        min=i
print(min)
print(max)
file.close()