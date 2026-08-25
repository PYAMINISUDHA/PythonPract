# num=[3,5,7,9,4,6,8]
# total=0
# file=open("integer_data","w")
# for i in num:
#     file.write(str(i)+"\n")
# file.close()
# file=open("integer_data","r")
# content=file.readlines()
# for i in content:
#     total+=int(i)
# print(total)
# file.close()

num=[3,5,7,9,4,6,8]
total=0
file=open("integer_data","w")
for i in num:
    file.write(str(i)+"\n")
file.close()
file=open("integer_data","r")
line=file.readline()
while line:
    total+=int(line)
    line=file.readline()
print(total)
file.close()