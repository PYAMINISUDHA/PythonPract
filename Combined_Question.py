sentance="python is easy and Python is powerful"
s=sentance.split(" ")
count=0
for i in s:
    if i.lower()=="python":
        count+=1
print(count)